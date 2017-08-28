from django.db import models
from django.contrib.auth.models import AbstractUser

from wagtail.wagtailcore.models import Site


class User(AbstractUser):
    """Base User Model for the CoSS project."""

    site = models.ForeignKey(Site, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('username', 'site',)
