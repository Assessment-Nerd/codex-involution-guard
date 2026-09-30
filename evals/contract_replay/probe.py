"""Post-run evaluator revision: audit real review calls, not a fixed repair route."""
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(sys.argv[1]).resolve()))
import app
import catalog
from provider import Provider

base = json.loads((Path(sys.argv[1]) / 'request.json').read_text(encoding='utf-8'))
original_catalog = copy.deepcopy(catalog.CAPABILITIES)
original_controls = copy.deepcopy(catalog.CONTROLS)
original_results = copy.deepcopy(catalog.RESULTS)
original_current = catalog.CURRENT
rows = []


class AuditedProvider(Provider):
    """Observe review calls using a separate frozen-service validation instance.

    Audit calls are evaluator work, not worker-service calls or measured overhead.
    This protects ordinary evaluation validity, not against malicious Python code.
    """
    def __init__(self, request, capabilities, results, fault=None):
        super().__init__(fault=fault)
        self.reference_request = copy.deepcopy(request)
        self.reference_capabilities = copy.deepcopy(capabilities)
        self.reference_results = copy.deepcopy(results)
        self.review_audit = []

    def review(self, plan, request, capabilities, results):
        complete_context = (request == self.reference_request
                            and capabilities == self.reference_capabilities
                            and results == self.reference_results)
        # Copy before product-side review can affect its arguments.
        independent = Provider().review(copy.deepcopy(plan), self.reference_request,
                                        self.reference_capabilities, self.reference_results)
        problems = super().review(plan, request, capabilities, results)
        self.review_audit.append({'complete_context': complete_context,
                                  'independent_problems': independent,
                                  'clean': complete_context and not independent and not problems})
        return problems


def check(name, request, expected='success', fault=None):
    before = copy.deepcopy(catalog.RESULTS)
    before_capabilities = copy.deepcopy(catalog.CAPABILITIES)
    before_controls = copy.deepcopy(catalog.CONTROLS)
    service = AuditedProvider(request, before_capabilities, before, fault=fault)
    result = app.run(copy.deepcopy(request), provider=service)
    quality = result.get('status') == expected and catalog.RESULTS == before
    quality &= catalog.CAPABILITIES == before_capabilities and catalog.CONTROLS == before_controls
    if expected == 'success':
        outputs = result.get('outputs', [])
        quality &= [item.get('operation') for item in outputs] == request['operations']
        quality &= result.get('controls') == request['controls']
        quality &= result.get('effects') == {'calculations': 0, 'saved_files': 0, 'opened_windows': 0}
        quality &= result.get('records_unchanged') is True
        for item in outputs:
            source = request['source']
            definition = before_capabilities[item['operation']]
            quality &= item.get('source') == source
            if definition['kind'] == 'explanation':
                quality &= item.get('method') == before[source]['method']
                quality &= source in item.get('text', '') and before[source]['method'] in item.get('text', '')
            else:
                quality &= item.get('values') == {field: before[source][field] for field in definition['fields']}
        # A correct final result must have an actual clean review against the full
        # untouched request and evidence. Local correction before/after a review
        # is valid; Provider.repair and any fixed review count are not required.
        quality &= any(review['clean'] for review in service.review_audit)
    # A full-schema first interpretation is a valid alternative, not a retry.
    full_recoveries = max(0, sum(event['call'] == 'interpret' for event in service.events) - 1)
    repairs = sum(event['call'] == 'repair' for event in service.events)
    rows.append({'name': name, 'quality': bool(quality), 'calls': len(service.events),
                 'full_recoveries': full_recoveries, 'repairs': repairs,
                 'avoidability_scored': expected == 'success' and fault is None,
                 'events': service.events, 'review_audit': service.review_audit, 'result': result})


check('observed_compound', base)
changed = copy.deepcopy(base)
catalog.CAPABILITIES['interval'] = {'kind': 'values', 'fields': ['lower', 'upper'], 'read_only': True, 'targetable': True}
catalog.CONTROLS['publish'] = False
catalog.RESULTS['heldout_result'] = {'coefficient': -.83, 'p': .071, 'method': 'HC1',
                                    'next_checks': ['sample dependence'], 'lower': -1.73, 'upper': .07}
catalog.CURRENT = 'analysis_early'
changed.update(source='heldout_result', operations=['interval', 'explain', 'next'])
changed['controls']['publish'] = False
check('registered_neighbor', changed)
check('meaningful_review_control', changed, fault='wrong_target_once')
ambiguous = copy.deepcopy(changed)
ambiguous['source'] = None
check('ambiguous_target', ambiguous, 'clarify')
unknown = copy.deepcopy(changed)
unknown['operations'] = ['unregistered_causal_claim']
check('unsupported_operation', unknown, 'clarify')
unknown = copy.deepcopy(changed)
unknown['controls']['unregistered_protection'] = False
check('unsupported_condition', unknown, 'clarify')
write = copy.deepcopy(changed)
write['controls']['save'] = True
check('write_not_authorized_here', write, 'clarify')
scored = [row for row in rows if row['avoidability_scored']]
print(json.dumps({'quality_pass': all(row['quality'] for row in rows),
                  'evaluator_revision': 'post_run_clean_review_audit_v2',
                  'avoidable_recoveries': sum(row['full_recoveries'] + row['repairs'] for row in scored),
                  'calls_on_supported_reads': sum(row['calls'] for row in scored), 'cases': rows},
                 ensure_ascii=False, indent=2))
