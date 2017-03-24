from django.db import models
from adminsortable.models import SortableMixin

from networkapi.utility.images import get_image_upload_path


def get_opportunities_image_upload_path(instance, filename):
    return get_image_upload_path(
        app_name='opportunities',
        prop_name='name',
        instance=instance,
        current_filename=filename
    )


class Opportunity(SortableMixin):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    link_label = models.CharField(max_length=300)
    link_url = models.URLField(max_length=2048)
    image = models.FileField(
        max_length=2048,
        upload_to=get_opportunities_image_upload_path,
    )
    order = models.PositiveIntegerField(
        default=0,
        editable=False,
        db_index=True,
    )
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'opportunities'
        ordering = ('order',)

    def __str__(self):
        return str(self.name)
