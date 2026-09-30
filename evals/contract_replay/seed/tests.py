import copy
import json
import unittest
from pathlib import Path
import app
import catalog


class ExistingBehavior(unittest.TestCase):
    def setUp(self):
        self.request = json.loads(Path(__file__).with_name('request.json').read_text(encoding='utf-8'))

    def test_compound_result(self):
        before = copy.deepcopy(catalog.RESULTS)
        result = app.run(self.request)
        self.assertEqual(result['status'], 'success')
        self.assertEqual(len(result['outputs']), 3)
        self.assertEqual(result['outputs'][1]['method'], 'HC3')
        self.assertEqual(result['controls'], self.request['controls'])
        self.assertEqual(catalog.RESULTS, before)

    def test_ambiguous_source_is_not_guessed(self):
        self.request['source'] = None
        self.assertEqual(app.run(self.request)['status'], 'clarify')


if __name__ == '__main__':
    unittest.main()
