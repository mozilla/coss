from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailcore import fields
from wagtail.wagtailsnippets.models import register_snippet

from coss.home.content_blocks import InputTextContentBlock, CardContentBlock, BottomCTAContentBlock


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
    bottom_content_block = fields.StreamField([
        ('cta', BottomCTAContentBlock(),),
    ], null=True, blank=True)
    optional_text_block_title = models.CharField(verbose_name='Title', blank=True, default='',
                                                 max_length=50)
    optional_text_block = fields.StreamField([
        ('secondary_section', InputTextContentBlock(),),
    ], null=True, blank=True, verbose_name='Blocks')

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
        StreamFieldPanel('bottom_content_block'),
        MultiFieldPanel([
            FieldPanel('optional_text_block_title'),
            StreamFieldPanel('optional_text_block'),
        ], heading='Secondary Input block'),
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
