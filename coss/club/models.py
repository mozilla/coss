from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField
from location_field.models.plain import PlainLocationField


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
