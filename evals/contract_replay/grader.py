"""Post-run evaluator revision and authored controls; no worker/model/API execution."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
FIXED_SCHEMA = '''def compact_schema():
    return {'name': 'compact', 'controls': list(catalog.CONTROLS), 'operations': {
        name: copy.deepcopy(definition) for name, definition in catalog.CAPABILITIES.items()
        if definition.get('read_only')}}
'''
FIXED_CONTEXT = "context = {'current': catalog.CURRENT, 'results': {source: copy.deepcopy(catalog.RESULTS[source]) for source in {catalog.CURRENT, request.get('source')} if source in catalog.RESULTS}}"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def grade(path):
    path = Path(path)
    protected = {name: (path / name).is_file() and sha(path / name) == sha(BASE / 'seed' / name)
                 for name in ('provider.py', 'request.json', 'tests.py')}
    def snapshot(root):
        return {str(file.relative_to(root)): sha(file) for file in root.rglob('*')
                if file.is_file() and '__pycache__' not in file.parts}
    with tempfile.TemporaryDirectory(prefix='contract-grade-') as temp:
        isolated = Path(temp) / 'work'
        shutil.copytree(path, isolated, ignore=shutil.ignore_patterns('__pycache__'))
        before = snapshot(isolated)
        completed = subprocess.run([sys.executable, str(BASE / 'probe.py'), str(isolated)], cwd=isolated,
                                   capture_output=True, text=True, encoding='utf-8', timeout=20)
        files_unchanged = snapshot(isolated) == before
    if completed.returncode:
        result = {'quality_pass': False, 'pass': False, 'execution_error': completed.stderr}
    else:
        result = json.loads(completed.stdout)
    result['provider_unchanged'] = protected['provider.py']
    result['protected_files'] = protected
    result['protected_files_unchanged'] = all(protected.values())
    result['files_unchanged'] = files_unchanged
    result['quality_pass'] &= result['protected_files_unchanged'] and files_unchanged
    result['pass'] = result['quality_pass'] and result.get('avoidable_recoveries') == 0
    result['evaluator_revision'] = 'post_run_clean_review_audit_v2'
    result['scope'] = 'integration recovery paths only, not live model latency'
    return result


def materialize_reference(path):
    shutil.copytree(BASE / 'seed', path)
    text = (path / 'app.py').read_text(encoding='utf-8')
    start = text.index('def compact_schema():')
    end = text.index('\n\ndef full_schema():', start)
    text = text[:start] + FIXED_SCHEMA + text[end:]
    old_context = "context = {'current': catalog.CURRENT, 'results': {catalog.CURRENT: catalog.RESULTS[catalog.CURRENT]}}"
    text = text.replace(old_context, FIXED_CONTEXT)
    (path / 'app.py').write_text(text, encoding='utf-8')


def selfcheck():
    with tempfile.TemporaryDirectory(prefix='contract-reference-') as temp:
        temp = Path(temp)
        ref = temp / 'reference'
        materialize_reference(ref)
        mutant = temp / 'symptom_only'
        shutil.copytree(BASE / 'seed', mutant)
        text = (mutant / 'app.py').read_text(encoding='utf-8')
        text = text.replace("['calculate', 'open_window']", "['calculate', 'save', 'open_window']")
        text = text.replace("context = {'current': catalog.CURRENT, 'results': {catalog.CURRENT: catalog.RESULTS[catalog.CURRENT]}}",
                            FIXED_CONTEXT)
        text = text.replace("'targetable': False", "'targetable': True")
        (mutant / 'app.py').write_text(text, encoding='utf-8')
        direct = temp / 'direct_full'
        shutil.copytree(ref, direct)
        text = (direct / 'app.py').read_text(encoding='utf-8').replace(
            'plan = service.interpret(request, compact_schema(), context)',
            'plan = service.interpret(request, full_schema(), context)')
        (direct / 'app.py').write_text(text, encoding='utf-8')
        # Legitimate correction routes that do not call Provider.repair.
        local = temp / 'local_repair'
        shutil.copytree(ref, local)
        local_fix = "plan = {'controls': request['controls'].copy(), 'unresolved': [], 'steps': [dict(operation=op, source=request['source'], **({'method': catalog.RESULTS[request['source']]['method']} if catalog.CAPABILITIES[op]['kind'] == 'explanation' else {})) for op in request['operations']]}"
        repair_call = 'plan = service.repair(plan, request, catalog.CAPABILITIES, catalog.RESULTS, problems)'
        text = (local / 'app.py').read_text(encoding='utf-8').replace(repair_call, local_fix)
        (local / 'app.py').write_text(text, encoding='utf-8')
        prevalidated = temp / 'prevalidated'
        shutil.copytree(ref, prevalidated)
        text = (prevalidated / 'app.py').read_text(encoding='utf-8').replace(
            '    problems = service.review(plan, request, catalog.CAPABILITIES, catalog.RESULTS)\n',
            '    ' + local_fix + '\n    problems = service.review(plan, request, catalog.CAPABILITIES, catalog.RESULTS)\n', 1)
        (prevalidated / 'app.py').write_text(text, encoding='utf-8')
        unreviewed = temp / 'unreviewed'
        shutil.copytree(prevalidated, unreviewed)
        text = (unreviewed / 'app.py').read_text(encoding='utf-8').replace(
            'problems = service.review(plan, request, catalog.CAPABILITIES, catalog.RESULTS)', 'problems = []')
        (unreviewed / 'app.py').write_text(text, encoding='utf-8')
        ignored = temp / 'ignored_review'
        shutil.copytree(local, ignored)
        text = (ignored / 'app.py').read_text(encoding='utf-8').replace(
            '        problems = service.review(plan, request, catalog.CAPABILITIES, catalog.RESULTS)',
            '        problems = []  # Incorrectly completes after repair without a clean review.')
        (ignored / 'app.py').write_text(text, encoding='utf-8')
        results = {'raw_seed': grade(BASE / 'seed'), 'reference': grade(ref),
                   'symptom_only': grade(mutant), 'valid_full_first': grade(direct),
                   'valid_local_repair': grade(local), 'valid_prevalidation': grade(prevalidated),
                   'invalid_unreviewed': grade(unreviewed), 'invalid_ignored_review': grade(ignored)}
        changed_request = temp / 'changed_request'
        shutil.copytree(ref, changed_request)
        request = (changed_request / 'request.json').read_text(encoding='utf-8')
        (changed_request / 'request.json').write_text(request + '\n', encoding='utf-8')
        changed_tests = temp / 'changed_tests'
        shutil.copytree(ref, changed_tests)
        (changed_tests / 'tests.py').write_text('# Original tests removed.\n', encoding='utf-8')
        results['invalid_changed_request'] = grade(changed_request)
        results['invalid_changed_tests'] = grade(changed_tests)
    assert results['raw_seed']['quality_pass'] and not results['raw_seed']['pass']
    assert results['reference']['pass']
    assert results['symptom_only']['quality_pass'] and not results['symptom_only']['pass']
    assert results['valid_full_first']['pass']
    assert results['valid_local_repair']['pass']
    assert results['valid_prevalidation']['pass']
    for name in ('valid_local_repair', 'valid_prevalidation'):
        fault_case = next(row for row in results[name]['cases'] if row['name'] == 'meaningful_review_control')
        assert fault_case['repairs'] == 0 and fault_case['quality']
    assert not results['invalid_unreviewed']['quality_pass']
    assert not results['invalid_ignored_review']['quality_pass']
    assert not results['invalid_changed_request']['protected_files']['request.json']
    assert not results['invalid_changed_tests']['protected_files']['tests.py']
    assert not results['invalid_changed_request']['pass'] and not results['invalid_changed_tests']['pass']
    return results


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('workspace', nargs='?')
    parser.add_argument('--selfcheck', action='store_true')
    parser.add_argument('--materialize-reference')
    parser.add_argument('--output')
    args = parser.parse_args()
    if args.materialize_reference:
        materialize_reference(Path(args.materialize_reference))
    else:
        output = json.dumps(selfcheck() if args.selfcheck else grade(Path(args.workspace)), ensure_ascii=False, indent=2)
        if args.output:
            Path(args.output).write_text(output, encoding='utf-8')
        print(output)
