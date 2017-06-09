from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # django-cities-light fields
    city = models.ForeignKey('cities_light.City', blank=True, null=True,
                             on_delete=models.SET_NULL)
    region = models.ForeignKey('cities_light.Region', blank=True, null=True,
                               on_delete=models.SET_NULL)
    country = models.ForeignKey('cities_light.Country', blank=True, null=True,
                                on_delete=models.SET_NULL)
