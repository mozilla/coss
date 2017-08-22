from django.test import TestCase

from coss.discourse.tests import DiscourseCategoryFactory

from unittest.mock import patch, PropertyMock


class DiscourseCategoryTests(TestCase):
    def setUp(self):
        self.category = DiscourseCategoryFactory.create()

    @patch('coss.discourse.models.DiscourseCategory.name', new_callable=PropertyMock)
    def test___str__(self, name):
        name.return_value = 'Category Name'

        self.assertEqual(str(self.category), 'Category Name')

    @patch('coss.discourse.models.DiscourseCategory._show')
    def test_name(self, _show):
        name = 'Category Name'
        _show.return_value = {'category': {'name': name}}

        self.assertEqual(self.category.name, name)

    @patch('coss.discourse.models.DiscourseCategory._latest')
    def test_latest_topics(self, _latest):
        _latest.return_value = {
            'topic_list': {
                'topics': [
                    {'pinned': True, 'last_posted_at': '1970-01-03T00:00:00.000Z'},
                    {'pinned': True, 'last_posted_at': '1970-01-01T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-05T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-04T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-02T00:00:00.000Z'},
                ]
            }
        }

        latest_topics = [
            {'pinned': False, 'last_posted_at': '1970-01-05T00:00:00.000Z'},
            {'pinned': False, 'last_posted_at': '1970-01-04T00:00:00.000Z'},
            {'pinned': True, 'last_posted_at': '1970-01-03T00:00:00.000Z'},
        ]

        self.assertEqual(self.category.latest_topics(3), latest_topics)

    @patch('coss.discourse.models.DiscourseCategory._latest')
    def test_latest_topics__no_pinned(self, _latest):
        topics = [
            {'pinned': False, 'last_posted_at': '1970-01-03T00:00:00.000Z'},
            {'pinned': False, 'last_posted_at': '1970-01-02T00:00:00.000Z'},
            {'pinned': False, 'last_posted_at': '1970-01-01T00:00:00.000Z'},
        ]

        _latest.return_value = {
            'topic_list': {
                'topics': topics
            }
        }

        self.assertEqual(self.category.latest_topics(3), topics)

    @patch('coss.discourse.models.DiscourseCategory._latest')
    def test_latest_topics__length(self, _latest):
        _latest.return_value = {
            'topic_list': {
                'topics': [
                    {'pinned': False, 'last_posted_at': '1970-01-05T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-04T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-03T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-02T00:00:00.000Z'},
                    {'pinned': False, 'last_posted_at': '1970-01-01T00:00:00.000Z'},
                ]
            }
        }

        self.assertEqual(len(self.category.latest_topics()), 3)
        self.assertEqual(len(self.category.latest_topics(1)), 1)
        self.assertEqual(len(self.category.latest_topics(10)), 5)

    @patch('coss.discourse.models.settings')
    @patch('coss.discourse.models.DiscourseCategory._cached_request')
    def test__show(self, _cached_request, settings):
        value = 'value'
        _cached_request.return_value = value
        settings.DISCOURSE_URL = 'http://discourse'

        self.assertEqual(self.category._show(), value)
        _cached_request.assert_called_once_with('http://discourse/c/198/show.json')

    @patch('coss.discourse.models.settings')
    @patch('coss.discourse.models.DiscourseCategory._cached_request')
    def test__latest(self, _cached_request, settings):
        value = 'value'
        _cached_request.return_value = value
        settings.DISCOURSE_URL = 'http://discourse'

        self.assertEqual(self.category._latest(), value)
        _cached_request.assert_called_once_with('http://discourse/c/198/none/l/latest.json')

    @patch('coss.discourse.models.cache')
    @patch('coss.discourse.models.requests')
    def test__cached_request__cached(self, requests, cache):
        path = 'path'
        value = 'value'

        cache.get.return_value = value

        self.assertEqual(self.category._cached_request(path), value)
        cache.get.assert_called_once_with(path)

    @patch('coss.discourse.models.cache')
    @patch('coss.discourse.models.requests')
    def test__cached_request__empty(self, requests, cache):
        path = 'path'
        value = 'value'

        cache.get.return_value = None
        requests.get.return_value.json.return_value = value

        self.assertEqual(self.category._cached_request(path), value)
        requests.get.assert_called_once_with(path)
