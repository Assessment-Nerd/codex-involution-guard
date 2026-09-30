"""Frozen deterministic external-service substitute, not an LLM or grader.

The recorded semantic request replaces language parsing. The service can emit only
represented operations/controls and uses only the supplied evidence context.
Keep this supplied adapter unchanged; product integration belongs in app.py/catalog.py.
"""
import copy


class Provider:
    def __init__(self, fault=None):
        self.events = []
        self.fault = fault

    def interpret(self, request, schema, context):
        self.events.append({'call': 'interpret', 'transport': schema['name']})
        if not request.get('source'):
            return {'clarify': 'Which stored analysis should be used?'}
        missing = [name for name in request['controls'] if name not in schema['controls']]
        missing += [op for op in request['operations'] if op not in schema['operations']]
        plan = {'controls': {k: v for k, v in request['controls'].items() if k in schema['controls']},
                'steps': [], 'unresolved': missing}
        for op in request['operations']:
            if op not in schema['operations']:
                continue
            definition = schema['operations'][op]
            source = request['source'] if definition.get('targetable') else context['current']
            step = {'operation': op, 'source': source}
            if definition['kind'] == 'explanation':
                record = context.get('results', {}).get(source, {})
                step['method'] = record.get('method')
            plan['steps'].append(step)
        if self.fault == 'wrong_target_once' and plan['steps'] and not plan['unresolved']:
            plan['steps'][0]['source'] = context['current']
            self.fault = None
        return plan

    def review(self, plan, request, capabilities, results):
        self.events.append({'call': 'review'})
        problems = []
        if plan.get('controls') != request['controls'] or plan.get('unresolved'):
            problems.append('unrepresented or missing source condition')
        steps = plan.get('steps', [])
        if [s['operation'] for s in steps] != request['operations']:
            problems.append('missing requested output')
        for step in steps:
            source = step['source']
            if source != request['source'] or source not in results:
                problems.append('wrong or missing analysis evidence')
                continue
            definition = capabilities.get(step['operation'])
            if not definition:
                problems.append('unsupported operation')
            elif definition['kind'] == 'explanation' and step.get('method') != results[source]['method']:
                problems.append('generic explanation not grounded in selected analysis')
        return problems

    def repair(self, plan, request, capabilities, results, problems):
        self.events.append({'call': 'repair', 'reasons': problems[:]})
        fixed = copy.deepcopy(plan)
        fixed['controls'] = request['controls'].copy()
        fixed['unresolved'] = []
        fixed['steps'] = []
        for op in request['operations']:
            step = {'operation': op, 'source': request['source']}
            if capabilities[op]['kind'] == 'explanation':
                step['method'] = results[request['source']]['method']
            fixed['steps'].append(step)
        return fixed
