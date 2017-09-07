from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore import fields
from wagtail.wagtailsnippets.models import register_snippet

from coss.home.content_blocks import InputTextContentBlock, CardContentBlock


class GroupsGatheringsLandingPage(Page):
    pass

    class Meta:
        verbose_name = 'Groups and Gatherings Landing Page'


@register_snippet
class AboutSnippet(models.Model):
    title = models.CharField(default='', max_length=50)
    header_text = fields.RichTextField(blank=True)
    body_title = models.CharField(verbose_name='Title', blank=True, default='',
                                  max_length=50)
    body_text = fields.RichTextField(verbose_name='Text', blank=True)
    body_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image'
    )
    info_title = models.CharField(verbose_name='Title', blank=True, default='',
                                  max_length=50)
    info_text = fields.RichTextField(verbose_name='Text', blank=True)
    details_title = models.CharField(verbose_name='Title', blank=True, default='',
                                     max_length=50)
    details = fields.StreamField([
        ('section', InputTextContentBlock(),),
    ], null=True, blank=True, verbose_name='Blocks')
    collaborators_title = models.CharField(verbose_name='Title', blank=True, default='',
                                           max_length=50)
    collaborators_text = fields.RichTextField(verbose_name='Text', blank=True)
    collaborators_cta_text = models.CharField(verbose_name='CTA Text', blank=True, default='',
                                              max_length=50)
    collaborators_cta_link = models.URLField(verbose_name='CTA Link', blank=True, default='')
    collaborators = fields.StreamField([
        ('info', CardContentBlock(),),
    ], null=True, blank=True)
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

    panels = [
        FieldPanel('title'),
        FieldPanel('header_text'),
        MultiFieldPanel([
            FieldPanel('body_title'),
            FieldPanel('body_text'),
            ImageChooserPanel('body_image'),
        ], heading='Body'),
        MultiFieldPanel([
            FieldPanel('info_title'),
            FieldPanel('info_text'),
        ], heading='Info'),
        MultiFieldPanel([
            FieldPanel('details_title'),
            StreamFieldPanel('details'),
        ], heading='Details'),
        MultiFieldPanel([
            FieldPanel('collaborators_title'),
            FieldPanel('collaborators_text'),
            FieldPanel('collaborators_cta_text'),
            FieldPanel('collaborators_cta_link'),
            StreamFieldPanel('collaborators'),
        ], heading='Collaborators Section'),
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
        ], heading='Bottom CTA Right Button'),
    ]

    class Meta:
        verbose_name_plural = 'About Snippets'

    def __str__(self):
        return self.title


@register_snippet
class Testimonial(models.Model):
    quote = fields.RichTextField()
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
