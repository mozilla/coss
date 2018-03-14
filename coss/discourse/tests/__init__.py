import factory

from coss.discourse.models import DiscourseCategory


class DiscourseCategoryFactory(factory.DjangoModelFactory):
    category_id = 198

    class Meta:
        model = DiscourseCategory
