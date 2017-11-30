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

from coss.base.models import CossBaseModel
from coss.home.content_blocks import InputTextContentBlock, CardContentBlock, BottomCTAContentBlock


UserModel = get_user_model()


# Generic models used in the app.
class ClubProfile(models.Model):
    """User profile relevant only to the Open Source Clubs."""
    user = models.OneToOneField(UserModel)
    title = models.CharField(max_length=128, blank=True, default='')
    is_captain = models.BooleanField(default=False)
    is_mentor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    # We define the panels here to exclude certain fields (avatar_url in this case)
    panels = [
        FieldPanel('user'),
        FieldPanel('title'),
        MultiFieldPanel([
            FieldPanel('is_captain'),
            FieldPanel('is_mentor'),
        ], heading='Club Profile attributes'),
    ]


class HomePage(Page, CossBaseModel):
    """Landing HomePage for OpenSource clubs."""

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    heading_text = fields.RichTextField(verbose_name='Text', blank=True, default='',)
    heading_cta_text = models.CharField(verbose_name='CTA Text', blank=True, default='',
                                        max_length=50)
    heading_cta_link = models.URLField(verbose_name='CTA Link', blank=True, default='')
    heading_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
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
    bottom_content_block = fields.StreamField([
        ('cta', BottomCTAContentBlock(),),
    ], null=True, blank=True)

    opengraph_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Open Graph Image'
    )

    def get_category_landing_page(self):
        if self.get_children().type(CategoryLandingPage):
            try:
                return CategoryLandingPage.objects.get()
            except (CategoryLandingPage.DoesNotExist, CategoryLandingPage.MultipleObjectsReturned):
                pass
        return CategoryLandingPage.objects.none()

    content_panels = Page.content_panels + [
        FieldPanel('logo'),
        FieldPanel('opengraph_image'),
        MultiFieldPanel([
            FieldPanel('heading_text'),
            FieldPanel('heading_cta_text'),
            FieldPanel('heading_cta_link'),
            FieldPanel('heading_image'),
        ], heading='Heading'),
        SnippetChooserPanel('discourse'),
        SnippetChooserPanel('testimonial'),
        StreamFieldPanel('bottom_content_block')
    ]


class CategoryLandingPage(Page, CossBaseModel):
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


class EntityTagIndexPage(Page, CossBaseModel):
    """Returns all the entities with the same tag."""

    def get_context(self, request):
        tag = request.GET.get('tag')
        entities = EntityDetailPage.objects.filter(tags__name=tag)

        context = super(EntityTagIndexPage, self).get_context(request)
        context['entities'] = entities
        return context


class EntityPageTag(TaggedItemBase):
    content_object = ParentalKey('EntityDetailPage', related_name='tagged_items')


class EntityDetailPage(Page, CossBaseModel):
    """Actual page for the Open Source clubs."""

    body_text = fields.RichTextField(blank=True)
    body_link = models.URLField(verbose_name='Description link', blank=True, default='')
    featured = models.BooleanField(default=False)
    is_flagged = models.BooleanField(default=False)
    club_name = models.CharField(max_length=128, default='')
    discourse_link = models.URLField(verbose_name='Discourse Link', blank=True, default='')
    contact_cta = models.URLField(verbose_name='Contact CTA link', blank=True)
    facebook_link = models.URLField(verbose_name='Facebook link', blank=True, default='')
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
        FieldPanel('body_text', classname='full'),
        FieldPanel('body_link'),
        FieldPanel('club_name'),
        FieldPanel('contact_cta'),
        FieldPanel('location'),
        MultiFieldPanel([
            FieldPanel('featured'),
            FieldPanel('is_flagged'),
        ], heading='Entity Attributes'),
        FieldPanel('flag_email'),
        FieldPanel('discourse_link'),
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


class AboutPage(Page, CossBaseModel):
    """About page for Open source clubs."""

    about = models.ForeignKey(
        'home.AboutSnippet',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    opengraph_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Open Graph Image'
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Logo'
    )
    featured = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        SnippetChooserPanel('about'),
        FieldPanel('opengraph_image'),
        FieldPanel('logo'),
        FieldPanel('featured')
    ]


class FAQPage(Page, CossBaseModel):
    """FAQ Page for Open Source Clubs."""
    faq = fields.StreamField([
        ('question', InputTextContentBlock(required=True),),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('faq'),
    ]


class ResourcesPage(Page, CossBaseModel):
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
    bottom_content_block = fields.StreamField([
        ('cta', BottomCTAContentBlock(),),
    ], null=True, blank=True)

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
        StreamFieldPanel('bottom_content_block'),
    ]


class ActivitiesPage(Page, CossBaseModel):
    """Activities Page for Open Source Clubs."""
    description = fields.RichTextField(blank=True)
    activity = fields.StreamField([
        ('info', CardContentBlock(required=True),)
    ])

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        StreamFieldPanel('activity'),
    ]
