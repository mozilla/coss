from django.db import models

from networkapi.utility.images import get_image_upload_path


def get_news_glyph_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='news',
        prop_name='headline',
        instance=instance,
        current_filename=filename
    )


class Topic(models.Model):
    """
    News Topics/Categories
    """
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.name)


class News(models.Model):
    """
    Medium blog posts and articles
    """
    headline = models.CharField(max_length=300)
    outlet = models.CharField(max_length=300)
    date = models.DateField()
    link = models.URLField(max_length=500)
    author = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    glyph = models.FileField(
        max_length=2048,
        upload_to=get_news_glyph_upload_path,
        null=True,
        blank=True,
    )
    topic = models.ForeignKey(
        Topic,
        related_name='news',
        null=True,
        on_delete=models.SET_NULL,
    )
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'news'
        ordering = ('-date',)

    def __str__(self):
        return str(self.headline)
