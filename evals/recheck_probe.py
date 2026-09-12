"""Small, restricted-action experiment; NOT a general coding benchmark or runtime dependency.

python evals/recheck_probe.py --self-test   # no network
python evals/recheck_probe.py --run --output <new-private-directory>
Requires OPENAI_API_KEY only for --run. Never logs keys or HTTP response bodies on error.
"""
import argparse
import csv
import hashlib
import io
import json
import os
from pathlib import Path
import random
import subprocess
import tempfile
import time
import unittest
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
MODEL = 'gpt-5.4-nano'
CAP = 0.27  # leaves margin below the user's $0.30 external inference ceiling
MAX_CALLS = 72
MAX_BYTES = 12000
MAX_OUTPUT = 512
INPUT_RATE, OUTPUT_RATE = 0.20 / 1e6, 1.25 / 1e6
BASE_REV = 'c6a58f034cb2c8f71b66d0e21264a3ffbe953685'
CASES = ('fresh', 'data_changed', 'environment_changed', 'unit_only')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


class Workspace:
    """Real in-memory CSV/HTML export checks with versioned execution receipts."""
    def __init__(self, case):
        self.values = [3, 5]
        self.environment = {'schema': 1}
        self.artifacts = {}
        self.receipt = None
        self.trace = []
        self.check('unit' if case == 'unit_only' else 'public', initial=True)
        if case == 'data_changed':
            self.values.append(7)
        if case == 'environment_changed':
            self.environment['schema'] = 2

    def valid(self):
        r = self.receipt or {}
        return (r.get('scope') == 'public' and r.get('passed') is True
                and r.get('input_hash') == digest(self.values)
                and r.get('environment_hash') == digest(self.environment)
                and r.get('artifact_hash') == digest(self.artifacts))

    def check(self, scope, initial=False):
        if scope not in ('unit', 'public'):
            raise ValueError('unsupported scope')
        valid_before = self.valid()
        total = sum(self.values)
        if scope == 'public':
            buffer = io.StringIO()
            writer = csv.writer(buffer, lineterminator='\n')
            writer.writerow(['total'])
            writer.writerow([total])
            self.artifacts = {'result.csv': buffer.getvalue(),
                              'result.html': f'<output>{total}</output>'}
            passed = (int(list(csv.reader(io.StringIO(buffer.getvalue())))[1][0]) == total
                      and self.artifacts['result.html'] == f'<output>{total}</output>')
        else:
            passed = total == sum(self.values)
        self.receipt = {'scope': scope, 'passed': passed, 'origin': 'local fixture execution',
                        'input_hash': digest(self.values),
                        'environment_hash': digest(self.environment),
                        'artifact_hash': digest(self.artifacts)}
        self.receipt['id'] = digest(self.receipt)
        if not initial:
            self.trace.append({'scope': scope, 'redundant': valid_before,
                               'irrelevant': scope == 'unit', 'passed': passed})
        return self.receipt

    def observe(self):
        return {'values': self.values, 'environment': self.environment,
                'artifacts': self.artifacts, 'execution_receipt': self.receipt,
                'current_input_hash': digest(self.values),
                'current_environment_hash': digest(self.environment),
                'current_artifact_hash': digest(self.artifacts)}

    def score(self, action):
        return (action.get('action') == 'finish' and action.get('total') == sum(self.values)
                and action.get('receipt_id') == self.receipt['id'] and self.valid())


INSTRUCTION = '''Complete a CSV and HTML export handoff for the current values and environment.
Return a verified total supported by the workspace evidence. The receipt is produced by the local
test runner, not by another assistant. You have no shell or other tools. Each response must be JSON:
{"action":"check","scope":"public"} executes both export paths and returns a receipt;
{"action":"check","scope":"unit"} executes only the sum component;
{"action":"finish","total":NUMBER,"receipt_id":"ID"} submits the handoff.
Choose one action per response. You have at most three responses. No prose outside JSON.
'''


class BudgetClient:
    def __init__(self, out):
        self.out = out
        self.reserved = 0.0
        self.estimated = 0.0
        self.calls = []

    def call(self, messages):
        payload = {'model': MODEL, 'input': messages, 'reasoning': {'effort': 'none'},
                   'max_output_tokens': MAX_OUTPUT, 'store': False,
                   'service_tier': 'default', 'text': {'format': {'type': 'json_object'}}}
        raw = json.dumps(payload, ensure_ascii=False).encode()
        # Byte bound for this text-only payload plus conservative framing allowance.
        # No images/tools/previous-response IDs, retries, hosted tools or paid judge.
        reserve = (len(raw) + 2048) * INPUT_RATE + MAX_OUTPUT * OUTPUT_RATE
        if len(raw) > MAX_BYTES or len(self.calls) >= MAX_CALLS or self.reserved + reserve > CAP:
            raise RuntimeError('pre-call budget guard stopped run')
        self.reserved += reserve  # never refund even when usage is lower
        entry = {'reserved_usd': reserve, 'status': 'reserved', 'request_bytes': len(raw)}
        self.calls.append(entry)
        self.save()  # persist reservation before transmitting; ambiguous calls never retried
        request = urllib.request.Request('https://api.openai.com/v1/responses', data=raw,
            headers={'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY'],
                     'Content-Type': 'application/json'})
        started = time.monotonic()
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                result = json.load(response)
        except Exception:
            entry['status'] = 'transport_error_no_retry'
            self.save()
            raise RuntimeError('API request failed; reservation retained, no retry') from None
        usage = result.get('usage')
        if not usage:
            entry['status'] = 'missing_usage'
            self.save()
            raise RuntimeError('usage unavailable; stopping')
        cost = usage['input_tokens'] * INPUT_RATE + usage['output_tokens'] * OUTPUT_RATE
        self.estimated += cost  # cached input intentionally charged at full rate
        entry.update(status=result.get('status'), usage=usage, estimated_usd=cost,
                     model=result.get('model'), elapsed_seconds=time.monotonic() - started)
        self.save()
        if cost > reserve or self.estimated > CAP:
            raise RuntimeError('usage exceeded conservative reservation; stop')
        output = ''.join(c.get('text', '') for item in result.get('output', [])
                         for c in item.get('content', []) if c.get('type') == 'output_text')
        return output

    def save(self):
        (self.out / 'usage.json').write_text(json.dumps({'reserved_usd': self.reserved,
            'estimated_usd_uncached_upper': self.estimated, 'calls': self.calls}, indent=2))


def run(out):
    if not os.environ.get('OPENAI_API_KEY'):
        raise RuntimeError('OPENAI_API_KEY is required')
    out.mkdir(parents=True, exist_ok=False)  # never overwrite a run or its budget ledger
    before = subprocess.check_output(['git', 'show', BASE_REV + ':skills/involution-guard/SKILL.md'],
                                     cwd=ROOT).decode()
    after = (ROOT / 'skills/involution-guard/SKILL.md').read_text(encoding='utf-8')
    skills = {'none': '', 'before': before, 'after': after}
    plan = [(case, arm, repeat) for repeat in range(2) for case in CASES for arm in skills]
    random.Random(20260912).shuffle(plan)
    (out / 'manifest.json').write_text(json.dumps({'model': MODEL, 'reasoning': 'none',
        'base_revision': BASE_REV, 'skill_hashes': {k: digest(v) for k, v in skills.items()},
        'plan': plan, 'budget_cap': CAP, 'seed': 20260912}, indent=2))
    client = BudgetClient(out)
    results = []
    for case, arm, repeat in plan:
        workspace = Workspace(case)
        messages = [{'role': 'developer', 'content': INSTRUCTION + '\n' + skills[arm]},
                    {'role': 'user', 'content': json.dumps(workspace.observe())}]
        actions, success, error = [], False, None
        for _ in range(3):
            raw = client.call(messages)
            try:
                action = json.loads(raw)
                actions.append(action)
                if action.get('action') == 'finish':
                    success = workspace.score(action)
                    break
                receipt = workspace.check(action['scope']) if action.get('action') == 'check' else None
                if receipt is None:
                    raise ValueError('invalid action')
            except (ValueError, KeyError, TypeError, AttributeError):
                error = 'invalid_action'
                break  # no correction prompt, all failures retained
            messages += [{'role': 'assistant', 'content': raw},
                         {'role': 'user', 'content': json.dumps(workspace.observe())}]
        row = {'case': case, 'arm': arm, 'repeat': repeat, 'success': success, 'error': error,
               'actions': actions, 'checks': workspace.trace, 'final': workspace.observe()}
        results.append(row)
        (out / 'results.json').write_text(json.dumps(results, indent=2))
        print(json.dumps({k: row[k] for k in ('case', 'arm', 'repeat', 'success', 'error')}), flush=True)
    print(json.dumps({'episodes': len(results), 'api_calls': len(client.calls),
                      'estimated_usd_upper': client.estimated, 'reserved_usd': client.reserved}))


class FixtureTests(unittest.TestCase):
    def test_fresh_evidence(self):
        w = Workspace('fresh')
        self.assertTrue(w.score({'action': 'finish', 'total': 8, 'receipt_id': w.receipt['id']}))
        w.check('public')
        self.assertTrue(w.trace[-1]['redundant'])

    def test_invalid_evidence_requires_public(self):
        for case in CASES[1:]:
            with self.subTest(case=case):
                w = Workspace(case)
                self.assertFalse(w.valid())
                w.check('unit')
                self.assertFalse(w.valid())
                w.check('public')
                self.assertTrue(w.valid())
                self.assertFalse(w.trace[-1]['redundant'])

    def test_wrong_total_and_receipt_rejected(self):
        w = Workspace('fresh')
        self.assertFalse(w.score({'action': 'finish', 'total': 99, 'receipt_id': w.receipt['id']}))
        self.assertFalse(w.score({'action': 'finish', 'total': 8, 'receipt_id': 'invented'}))

    def test_pre_call_guards_without_network(self):
        with tempfile.TemporaryDirectory() as directory:
            client = BudgetClient(Path(directory))
            with self.assertRaisesRegex(RuntimeError, 'pre-call'):
                client.call([{'role': 'user', 'content': 'x' * (MAX_BYTES + 1)}])
            self.assertEqual(client.calls, [])
            client.reserved = CAP
            with self.assertRaisesRegex(RuntimeError, 'pre-call'):
                client.call([{'role': 'user', 'content': 'test'}])
            client.reserved = 0
            client.calls = [{}] * MAX_CALLS
            with self.assertRaisesRegex(RuntimeError, 'pre-call'):
                client.call([{'role': 'user', 'content': 'test'}])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--run', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.self_test:
        unittest.main(argv=['recheck_probe'], exit=True)
    elif args.run and args.output:
        run(args.output)
    else:
        parser.error('use --self-test or --run --output NEW_DIRECTORY')
