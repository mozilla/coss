from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class ClubPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full')
    ]


class ClubsLandingPage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
    ]
