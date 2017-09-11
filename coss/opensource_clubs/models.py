from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                StreamFieldPanel, MultiFieldPanel)
from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from coss.home.content_blocks import InputTextContentBlock, CardContentBlock


UserModel = get_user_model()


class HomePage(Page):
    """Landing HomePage for OpenSource clubs."""

    heading_text = fields.RichTextField(verbose_name='Text', blank=True, default='',)
    heading_cta_text = models.CharField(verbose_name='CTA Text', blank=True, default='',
                                        max_length=50)
    heading_cta_link = models.URLField(verbose_name='CTA Link', blank=True, default='')
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
    bottom_cta_title = models.CharField(verbose_name='Title', blank=True, default='',
                                        max_length=50)
    bottom_cta_text = models.CharField(verbose_name='Text', blank=True, default='',
                                       max_length=100)
    bottom_cta1_text = models.CharField(verbose_name='Text', blank=True, default='',
                                        max_length=20)
    bottom_cta1_link = models.URLField(verbose_name='Link', blank=True, default='')
    bottom_cta2_text = models.CharField(verbose_name='Text', blank=True, default='',
                                        max_length=20)
    bottom_cta2_link = models.URLField(verbose_name='Link', blank=True, default='')

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
        MultiFieldPanel([
            FieldPanel('heading_text'),
            FieldPanel('heading_cta_text'),
            FieldPanel('heading_cta_link'),
        ], heading='Heading'),
        SnippetChooserPanel('discourse'),
        SnippetChooserPanel('testimonial'),
        MultiFieldPanel([
            FieldPanel('bottom_cta_title'),
            FieldPanel('bottom_cta_text'),
        ], heading='Bottom CTA'),
        MultiFieldPanel([
            FieldPanel('bottom_cta1_text'),
            FieldPanel('bottom_cta1_link'),
        ], heading='Bottom CTA Left button'),
        MultiFieldPanel([
            FieldPanel('bottom_cta2_text'),
            FieldPanel('bottom_cta2_link'),
        ], heading='Bottom CTA Right Button')
    ]


class CategoryLandingPage(Page):
    """Category Landing page for Open Source Clubs."""
    heading_text = fields.RichTextField(verbose_name='Text', blank=True, default='',)
    heading_cta_text = models.CharField(verbose_name='CTA Text', blank=True, default='',
                                        max_length=50)
    heading_cta_link = models.URLField(verbose_name='CTA Link', blank=True, default='')

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading_text'),
            FieldPanel('heading_cta_text'),
            FieldPanel('heading_cta_link'),
        ], heading='Heading'),
    ]


class EntityDetailPage(Page):
    """Actual page for the Open Source clubs."""
    description = fields.RichTextField(blank=True)
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
    """Image gallery for the Open Source Clubs."""

    page = ParentalKey(EntityDetailPage, related_name='gallery_images')
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
    caption = models.CharField(blank=True, default='', max_length=512)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption')
    ]


class AboutPage(Page):
    """About page for Open source clubs."""

    about = models.ForeignKey(
        'home.AboutSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel('about'),
    ]


class FAQPage(Page):
    """FAQ Page for Open Source Clubs."""
    faq = fields.StreamField([
        ('question', InputTextContentBlock(required=True),),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('faq'),
    ]


class ActivitiesPage(Page):
    """Activities Page for Open Source Clubs."""
    description = fields.RichTextField(blank=True)
    activity = fields.StreamField([
        ('info', CardContentBlock(required=True),)
    ])

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        StreamFieldPanel('activity'),
    ]


class ClubProfile(models.Model):
    """User profile relevant only to the Open Source Clubs."""
    user = models.OneToOneField(UserModel)
    is_captain = models.BooleanField(default=False)
