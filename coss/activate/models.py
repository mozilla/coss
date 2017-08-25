from __future__ import absolute_import, unicode_literals

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page


class ActivateHomePage(Page):
    description = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        FieldPanel('body', classname='full'),
    ]

    class Meta:
        verbose_name = 'Activate HomePage'
