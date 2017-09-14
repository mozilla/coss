from __future__ import absolute_import, unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                StreamFieldPanel, MultiFieldPanel)

from wagtail.wagtailcore import fields
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from coss.home.content_blocks import InputTextContentBlock, CardContentBlock
from coss.opensource_clubs import forms


UserModel = get_user_model()


# Generic models used in the app.
class ClubProfile(models.Model):
    """User profile relevant only to the Open Source Clubs."""
    user = models.OneToOneField(UserModel)
    is_captain = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)
    title = models.CharField(max_length=128, blank=True, default='')
    github_link = models.URLField(max_length=128, blank=True, default='')
    mozillian_username = models.CharField(max_length=40, default='')
    avatar_url = models.URLField(max_length=400, default='', blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    # We define the panels here to exclude certain fields (avatar_url in this case)
    panels = [
        FieldPanel('user'),
        FieldPanel('title'),
        FieldPanel('github_link'),
        FieldPanel('mozillian_username'),
        MultiFieldPanel([
            FieldPanel('is_captain'),
            FieldPanel('is_mentor'),
        ], heading='Club Profile attributes'),
    ]

    base_form_class = forms.ClubProfileForm


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
        return EntityDetailPage.objects.filter(featured=True).order_by('?')[:3]

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


class EntityTagIndexPage(Page):
    """Returns all the entities with the same tag."""

    def get_context(self, request):
        tag = request.GET.get('tag')
        entities = EntityDetailPage.objects.filter(tags__name=tag)

        context = super(EntityTagIndexPage, self).get_context(request)
        context['entities'] = entities
        return context


class EntityPageTag(TaggedItemBase):
    content_object = ParentalKey('EntityDetailPage', related_name='tagged_items')


class EntityDetailPage(Page):
    """Actual page for the Open Source clubs."""

    description = fields.RichTextField(blank=True)
    featured = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    club_name = models.CharField(max_length=128, default='')
    discourse_link = models.URLField(verbose_name='Discourse Link', blank=True, default='')
    contact_cta = models.URLField(verbose_name='Contact CTA link', blank=True)
    description_link = models.URLField(verbose_name='Description link', blank=True, default='')
    facebook_link = models.URLField(verbose_name='Facebook link', blank=True, default='')
    contact_cta = models.URLField(verbose_name='Description social link', blank=True, default='')
    members = ParentalManyToManyField(ClubProfile, blank=True, related_name='profiles')
    tags = ClusterTaggableManager(through=EntityPageTag, blank=True)
    location = models.CharField(max_length=255, blank=True, default='')
    flag_email = models.EmailField(blank=True, default='')

    def get_first_image(self):
        item = self.gallery_images.first()
        if item:
            return item.image
        return None

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        FieldPanel('club_name'),
        FieldPanel('contact_cta'),
        FieldPanel('location'),
        MultiFieldPanel([
            FieldPanel('featured'),
            FieldPanel('is_flagged'),
        ], heading='Entity Attributes'),
        FieldPanel('flag_email'),
        FieldPanel('discourse_link'),
        FieldPanel('description_link'),
        FieldPanel('facebook_link'),
        FieldPanel('tags'),
        InlinePanel('gallery_images', label='Gallery Images'),
        FieldPanel('members'),
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


class ResourcesPage(Page):
    """Resources Page for Open Source Clubs."""
    heading_text = fields.RichTextField(verbose_name='Text', blank=True)
    heading_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Image'
    )
    mentors_description = fields.StreamField([
        ('info', InputTextContentBlock(required=True),),
    ])
    resources_title = models.CharField(verbose_name='Title', blank=True, default='',
                                       max_length=50)
    resources_cta_text = models.CharField(verbose_name='CTA Text', blank=True, default='',
                                          max_length=50)
    resources_cta_link = models.URLField(verbose_name='Link', blank=True, default='')
    guides = fields.RichTextField(verbose_name='Guides', blank=True)

    def get_mentors(self):
        # TODO: Add filter for mentors that belong to each club
        return ClubProfile.objects.filter(is_mentor=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('heading_text'),
            FieldPanel('heading_image'),
        ], heading='Heading'),
        StreamFieldPanel('mentors_description'),
        MultiFieldPanel([
            FieldPanel('resources_title'),
            FieldPanel('resources_cta_text'),
            FieldPanel('resources_cta_link'),
            FieldPanel('guides'),
        ], heading='Resources'),
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
