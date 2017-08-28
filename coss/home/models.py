from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet


class GroupsGatheringsLandingPage(Page):
    pass

    class Meta:
        verbose_name = 'Groups and Gatherings Landing Page'


@register_snippet
class AboutSnippet(models.Model):
    header_text = RichTextField(blank=True)
    body_title = models.CharField(blank=True, default='', max_length=40)
    body_text = RichTextField(blank=True)
    info_title = models.CharField(blank=True, default='', max_length=40)
    info_text = RichTextField(blank=True)

    panels = [
        FieldPanel('header_text'),
        FieldPanel('body_title'),
        FieldPanel('body_text'),
        FieldPanel('info_title'),
        FieldPanel('info_text'),
    ]

    class Meta:
        verbose_name_plural = 'About Snippets'

    def __str__(self):
        return self.header_text
