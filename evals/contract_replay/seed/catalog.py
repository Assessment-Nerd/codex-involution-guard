"""The executor's existing supported read capabilities and side-effect controls."""
CAPABILITIES = {
    'read': {'kind': 'values', 'fields': ['coefficient', 'p'], 'read_only': True, 'targetable': True},
    'explain': {'kind': 'explanation', 'fields': ['method'], 'read_only': True, 'targetable': True},
    'next': {'kind': 'values', 'fields': ['next_checks'], 'read_only': True, 'targetable': True}}
CONTROLS = {'calculate': False, 'save': False, 'open_window': False}
RESULTS = {
    'analysis_early': {'coefficient': .9891, 'p': .0001, 'method': 'HC3',
                       'next_checks': ['residual assumptions'], 'lower': .72, 'upper': 1.24},
    'analysis_latest': {'coefficient': 1.44, 'p': .021, 'method': 'classical',
                        'next_checks': ['influence'], 'lower': 1.09, 'upper': 1.79}}
CURRENT = 'analysis_latest'
