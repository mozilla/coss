from django.db import models
from django.core.cache import cache
from django.conf import settings

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet

import requests


@register_snippet
class DiscourseCategory(models.Model):
    category_id = models.PositiveSmallIntegerField()

    panels = [
        FieldPanel('category_id')
    ]

    class Meta:
        verbose_name_plural = 'discourse categories'

    def __str__(self):
        return str(self.name)

    @property
    def name(self):
        return self._show()['category']['name']

    def latest_topics(self, n=3):
        latest = self._latest()
        topics = latest['topic_list']['topics']
        n_pinned = len(list(filter(lambda topic: topic['pinned'], topics)))
        topics = topics[:n + n_pinned]
        topics.sort(key=lambda t: t['last_posted_at'], reverse=True)
        return topics[:n]

    def _show(self):
        return self._cached_request(f'{settings.DISCOURSE_URL}/c/{self.category_id}/show.json')

    def _latest(self):
        return self._cached_request(f'{settings.DISCOURSE_URL}/c/{self.category_id}' +
                                    '/none/l/latest.json')

    def _cached_request(self, path):
        value = cache.get(path)
        if value is None:
            r = requests.get(path)
            value = r.json()
            cache.set(path, value)
        return value
