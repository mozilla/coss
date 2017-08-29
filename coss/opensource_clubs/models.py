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
    testimonial = models.ForeignKey(
        'home.Testimonial',
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
        try:
            return CategoryLandingPage.objects.get()
        except:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        SnippetChooserPanel('discourse'),
        SnippetChooserPanel('testimonial'),
    ]


class CategoryLandingPage(Page):
    heading = models.CharField(max_length=150, default='')
    testimonial = models.ForeignKey(
        'home.Testimonial',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('heading'),
        SnippetChooserPanel('testimonial'),
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


class AboutPage(Page):
    about = models.ForeignKey(
        'home.AboutSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    roles_captain = RichTextField(blank=True)
    roles_coordinator = RichTextField(blank=True)
    roles_member = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        SnippetChooserPanel('about'),
        FieldPanel('roles_captain', classname='full'),
        FieldPanel('roles_coordinator', classname='full'),
        FieldPanel('roles_member', classname='full'),
    ]


class EntityImageGallery(Orderable):

    page = ParentalKey(EntityDetailPage, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, default='', max_length=512)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]
