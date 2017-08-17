from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


class CategoryLandingPage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
    ]


class EntityDetailPage(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        InlinePanel('gallery_images', label='Gallery Images')
    ]


class EntityImageGallery(Orderable):

    page = ParentalKey(EntityDetailPage, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, default='', max_length=512)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]
