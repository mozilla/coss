from django.db import models
from django.contrib.auth.models import AbstractUser

from wagtail.wagtailcore.models import Site


class User(AbstractUser):
    """Base User Model for the CoSS project."""

    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)
    # This field is not exposed in the form.
    # It's populate from the mozillians API
    avatar = models.URLField(max_length=400, default='', blank=True)
    # When IAM is connected to CoSS this should be automatically populated
    github = models.URLField(max_length=128, blank=True, default='')

    class Meta:
        unique_together = ('username', 'site',)
