from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField
from location_field.models.plain import PlainLocationField


class FooterLink(models.Model):
  linktext = models.CharField(max_length=500)
  # the following can't be a URLField because it also needs to
  # do things like relative links and mailto
  link = models.CharField(max_length=2048)
  iconclass = models.CharField(max_length=2048)

  def __str__(self):
    return str(self.linktext)

class BasketNewsletter(models.Model):
  name = models.CharField(max_length=140)

  def __str__(self):
    return str(self.name)

class Signup(models.Model):
  header = models.CharField(max_length=500)
  description = RichTextField("description")
  newsletter = models.ForeignKey(
    BasketNewsletter,
    related_name='form',
    null=True,
    on_delete=models.PROTECT
  )

  def __str__(self):
    return str(self.header)


class PageWithCallout(Page):
  name = models.CharField(max_length=500)

  LABELS = (
    ('read', 'Read and contribute'),
    ('write', 'Create and inspire'),
  )

  label = models.CharField(
      max_length=12,
      choices=LABELS,
      default='read',
  )

  # featured-image = s3boto3 stuffs

  featured = models.BooleanField(default=False)

  header = models.CharField(max_length=500)
  content = RichTextField("Main body content")

  signup = models.ForeignKey(
      Signup,
      related_name='page',
      null=True,
      on_delete=models.SET_NULL,
  )

  def __str__(self):
    return str(self.name)

  def get_footer_links(self):
    return FooterLink.objects.all()
