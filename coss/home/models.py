from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsnippets.models import register_snippet


class GroupsGatheringsLandingPage(Page):
    pass

    class Meta:
        verbose_name = 'Groups and Gatherings Landing Page'


@register_snippet
class AboutSnippet(models.Model):
    title = models.CharField(default='', max_length=40)
    header_text = RichTextField(blank=True)
    body_title = models.CharField(blank=True, default='', max_length=40)
    body_text = RichTextField(blank=True)
    info_title = models.CharField(blank=True, default='', max_length=40)
    info_text = RichTextField(blank=True)
    bottom_cta_title = models.CharField('Title', blank=True, default='', max_length=40)
    bottom_cta_text = models.CharField('Text', blank=True, default='', max_length=40)
    bottom_cta1_text = models.CharField('Text', blank=True, default='', max_length=20)
    bottom_cta1_link = models.URLField('Link', blank=True, default='')
    bottom_cta2_text = models.CharField('Text', blank=True, default='', max_length=20)
    bottom_cta2_link = models.URLField('Link', blank=True, default='')

    panels = [
        FieldPanel('title'),
        FieldPanel('header_text'),
        FieldPanel('body_title'),
        FieldPanel('body_text'),
        FieldPanel('info_title'),
        FieldPanel('info_text'),
        MultiFieldPanel([
            FieldPanel('bottom_cta_title'),
            FieldPanel('bottom_cta_text'),
        ], heading="Bottom CTA"),
        MultiFieldPanel([
            FieldPanel('bottom_cta1_text'),
            FieldPanel('bottom_cta1_link'),
        ], heading="Bottom CTA Left button"),
        MultiFieldPanel([
            FieldPanel('bottom_cta2_text'),
            FieldPanel('bottom_cta2_link'),
        ], heading="Bottom CTA Right Button"),
    ]

    class Meta:
        verbose_name_plural = 'About Snippets'

    def __str__(self):
        return self.title


@register_snippet
class Testimonial(models.Model):
    quote = RichTextField()
    person = models.CharField(max_length=100)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('quote'),
        FieldPanel('person'),
        ImageChooserPanel('photo'),
    ]

    def __str__(self):
        return self.person
