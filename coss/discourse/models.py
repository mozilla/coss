from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class DiscourseCategory(models.Model):
    category_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=50, blank=True, default='')

    panels = [
        FieldPanel('category_id')
    ]

    class Meta:
        verbose_name_plural = 'discourse categories'

    def __str__(self):
        return str(self.name)
