import json
from unittest import TestCase
import requests
from gh2insertworker.builder import build_data
import mock

MOCK_DATA = [(u'weight', u'nsri', 6, 'parent'),
(u'physical_object', u'difficulti', 6, 'parent'),
(u'object', u'arriv', 6, 'parent'),
(u'abstraction', u'shelli', 6, 'parent'),
(u'conveyance', u'craft', 6, 'parent'),
(u'watercraft', u'alarm', 6, 'parent'),
(u'abstraction', u'beach', 6, 'parent'),
(u'instrumentation', u'craft', 6, 'parent'),
(u'instrumentality', u'difficulti', 6, 'parent'),
(u'fright', u'boat', 6, 'parent'),
(u'watercraft', u'alert', 6, 'parent'),
(u'time_unit', u'boat', 6, 'parent'),
(u'time_period', u'boat', 6, 'parent'),
(u'instrumentation', u'port', 6, 'parent'),
(u'papers', u'shelli', 6, 'parent'),
(u'vessel', u'bay.', 6, 'parent'),
(u'watercraft', u'report', 6, 'parent'),
(u'line', u'boat', 6, 'parent'),
(u'social_unit', u'boat', 6, 'parent')]

class TestBuilder(TestCase):

    def test_build_data(self):
        http_client = requests
        response = build_data(http_client, '94', MOCK_DATA)
        self.assertTrue(response)

