from django.db import models

from mezzanine.core.fields import RichTextField
from mezzanine.core.models import RichText
from mezzanine.pages.models import Page

from location_field.models.plain import PlainLocationField


class ClubRegistration(models.Model):
    OPENSOURCE = 'OSS'
    WEBLITERACY = 'WEB'
    WOMENCHILDREN = 'WNC'
    CLUB_TYPE = (
        (OPENSOURCE, 'Open Source'),
        (WEBLITERACY, 'Web Literacy'),
        (WOMENCHILDREN, 'Women & Children'),
    )

    CLUB_NEW = 'new'
    CLUB_EXISTING = 'existing'
    CLUB_UNKNOWN = 'notsure'
    CLUB_STATUS = (
        (CLUB_NEW, 'New Club'),
        (CLUB_EXISTING, 'Existing Club'),
        (CLUB_UNKNOWN, 'Not Sure'),
    )

    PUBLIC = 'public'
    OPEN = 'open'
    PRIVATE = 'private'
    CLUB_PRIVACY = (
        (PUBLIC, 'Public Visibility'),
        (OPEN, 'Anyone Can Join'),
        (PRIVATE, 'Private & Closed'),
    )

    club_type = models.CharField(max_length=40, choices=CLUB_TYPE, default=OPENSOURCE)
    club_status = models.CharField(max_length=40, choices=CLUB_STATUS, default=CLUB_NEW)
    club_name = models.CharField(max_length=40)
    club_description = RichTextField()
    club_location = models.CharField(max_length=255)
    club_place = models.CharField(max_length=255)
    club_privacy = models.CharField(max_length=40, choices=CLUB_PRIVACY, default=PUBLIC)
    fullname = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    occupation = models.CharField(max_length=255, blank=True)
    github_username = models.CharField(max_length=255, blank=True)


# Interest (subjects) that can apply to a club
class InterestQuerySet(models.query.QuerySet):
    def public(self):
        return self


class Interest(models.Model):
    name = models.CharField(unique=True, max_length=150)
    objects = InterestQuerySet.as_manager()

    def __str__(self):
        return str(self.name)


# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For clubs we can use the title field to
# store the club's name. For our model definition, we just add
# any extra fields that aren't part of the Page model.
class ClubQuerySet(models.query.QuerySet):
    def public(self):
        return self


class Testimonial(models.Model):
    """Testimonial model."""
    photo = models.ImageField()
    quote = RichTextField('Testimonial quote')

    def __str__(self):
        return str(self.quote)


class Club(Page):

    club_description = RichTextField("club description")
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)

    # Users associated with this club
    # - captain
    # - coordinator
    # - member

    ACTIVITY = (
        ('daily', 'Every day'),
        ('weekly', 'Once a week'),
        ('fortnightly', 'Once per two weeks'),
        ('monthly', 'Once per month'),
        ('infrequently', 'Less than once a month'),
        ('not', 'This club has shut down'),
    )

    activity = models.CharField(
        max_length=12,
        choices=ACTIVITY,
        default='weekly',
    )

    # events tied to this club
    # - events

    interests = models.ManyToManyField(
        Interest,
        related_name='club',
        blank=True
    )

    affiliated = models.CharField(
        max_length=500,
        blank=True
    )

    objects = ClubQuerySet.as_manager()

    def __str__(self):
        return str(self.title)


class Signup(Page):
    """Signup model."""
    heading = models.CharField(max_length=200, help_text='Signup heading')


class HomePage(Page, RichText):
    """Base homepage model."""

    # Header configuration
    header_heading = models.CharField(max_length=200,
                                      help_text='The heading of the header.')
    header_subheading = models.CharField(max_length=200,
                                         help_text='The heading of the sub-header.')
    header_text = RichTextField('Header text.')
    header_link = models.CharField(max_length=200,
                                   help_text='Header link.')

    # testimonial
    testimonial = models.ForeignKey('Testimonial',
                                    null=True,
                                    blank=True,
                                    help_text='Choose a testimonial quote to display')

    # club block
    featured_club = models.ForeignKey('Club',
                                      null=True,
                                      blank=True,
                                      help_text='Items from a club will be shown on the home page')


class SingleColumn(Page, RichText):
    """Single Column model."""
    # Text blocks
    club_elements = RichTextField('Elements of a Club')
    club_roles = RichTextField('Club Roles')
    club_types = RichTextField('Types of Clubs')

    # Regional coordinators link
    regional_link_text = models.CharField(max_length=200,
                                          help_text='Link Text')
    regional_link_url = models.CharField(max_length=200,
                                         help_text='Link URL')
