from django.db import models
from adminsortable.models import SortableMixin

from networkapi.utility.images import get_image_upload_path


def get_people_image_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='people',
        prop_name='name',
        instance=instance,
        current_filename=filename
    )


def get_people_partnership_logo_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='people',
        prop_name='name',
        suffix='_partnership',
        instance=instance,
        current_filename=filename
    )


class InternetHealthIssue(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Person(SortableMixin):
    """
    A member of the Network
    """
    name = models.CharField(max_length=300)
    role = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    quote = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
    )
    bio = models.TextField(
        max_length=5000,
        null=True,
        blank=True,
    )
    # We use FileField instead of ImageField since Django does not support
    # svgs for the ImageField
    image = models.FileField(
        max_length=2048,
        upload_to=get_people_image_upload_path
    )
    partnership_logo = models.FileField(
        max_length=2048,
        upload_to=get_people_partnership_logo_upload_path,
        null=True,
        blank=True,
    )
    twitter_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
    )
    linkedin_url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
    )
    internet_health_issues = models.ManyToManyField(
        InternetHealthIssue,
        related_name='people'
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'people'
        ordering = ('order',)

    def __str__(self):
        return str(self.name)


class Affiliation(models.Model):
    name = models.CharField(max_length=300)
    person = models.ForeignKey(
        Person,
        related_name='affiliations',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.name)
