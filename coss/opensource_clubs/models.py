from __future__ import absolute_import, unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel


class HomePage(Page):
    description = RichTextField(blank=True)
    discourse = models.ForeignKey(
        'discourse.DiscourseCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_featured(self):
        items = EntityDetailPage.objects.filter(featured=True)
        if items:
            return items
        return None

    def get_category_page(self):
        return CategoryLandingPage.objects.get()

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        SnippetChooserPanel('discourse')
    ]


class CategoryLandingPage(Page):
    heading = models.CharField(max_length=150, default='')

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
    ]


class EntityDetailPage(Page):
    description = RichTextField(blank=True)
    featured = models.BooleanField(default=False)

    def get_first_image(self):
        item = self.gallery_images.first()
        if item:
            return item.image
        return None

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        FieldPanel('featured'),
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
