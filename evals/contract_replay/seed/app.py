"""Read-only compound followups through interpretation, review and existing execution."""
import copy
import json
import sys
import catalog
from provider import Provider


def compact_schema():
    return {'name': 'compact', 'controls': ['calculate', 'open_window'], 'operations': {
        'read': {'kind': 'values', 'fields': ['coefficient', 'p'], 'targetable': True},
        'explain': {'kind': 'explanation', 'fields': ['method'], 'targetable': True},
        'next': {'kind': 'values', 'fields': ['next_checks'], 'targetable': False}}}


def full_schema():
    return {'name': 'full', 'controls': list(catalog.CONTROLS),
            'operations': copy.deepcopy(catalog.CAPABILITIES)}


def execute(plan):
    output = []
    for step in plan['steps']:
        definition = catalog.CAPABILITIES[step['operation']]
        record = catalog.RESULTS[step['source']]
        item = {'operation': step['operation'], 'source': step['source']}
        if definition['kind'] == 'explanation':
            item['method'] = step['method']
            item['text'] = f"Stored analysis {step['source']} used {step['method']}. Standard-error choice is not a new coefficient calculation."
        else:
            item['values'] = {field: copy.deepcopy(record[field]) for field in definition['fields']}
        output.append(item)
    return output


def run(request, provider=None):
    service = provider or Provider()
    original = copy.deepcopy(catalog.RESULTS)
    if any(op not in catalog.CAPABILITIES for op in request['operations']):
        return {'status': 'clarify', 'question': 'Requested output is not registered.', 'events': service.events}
    if request.get('source') and request['source'] not in catalog.RESULTS:
        return {'status': 'clarify', 'question': 'Stored analysis was not found.', 'events': service.events}
    if any(name not in catalog.CONTROLS for name in request['controls']):
        return {'status': 'clarify', 'question': 'Requested constraint is not registered.', 'events': service.events}
    if any(value is not False for value in request['controls'].values()):
        return {'status': 'clarify', 'question': 'This entrypoint only reads existing results.', 'events': service.events}
    context = {'current': catalog.CURRENT, 'results': {catalog.CURRENT: catalog.RESULTS[catalog.CURRENT]}}
    plan = service.interpret(request, compact_schema(), context)
    if 'clarify' in plan:
        return {'status': 'clarify', 'question': plan['clarify'], 'events': service.events}
    if plan.get('unresolved'):
        plan = service.interpret(request, full_schema(), context)
    problems = service.review(plan, request, catalog.CAPABILITIES, catalog.RESULTS)
    if problems:
        plan = service.repair(plan, request, catalog.CAPABILITIES, catalog.RESULTS, problems)
        problems = service.review(plan, request, catalog.CAPABILITIES, catalog.RESULTS)
    if problems:
        return {'status': 'blocked', 'issues': problems, 'events': service.events}
    return {'status': 'success', 'outputs': execute(plan), 'controls': plan['controls'],
            'effects': {'calculations': 0, 'saved_files': 0, 'opened_windows': 0},
            'records_unchanged': catalog.RESULTS == original, 'events': service.events}


if __name__ == '__main__':
    with open(sys.argv[1] if len(sys.argv) > 1 else 'request.json', encoding='utf-8') as stream:
        print(json.dumps(run(json.load(stream)), ensure_ascii=False, indent=2))
