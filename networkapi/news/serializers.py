from rest_framework import serializers

from networkapi.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    """
    Serializes a News object
    """
    topic = serializers.StringRelatedField()

    class Meta:
        model = News
        fields = (
            'headline',
            'outlet',
            'topic',
            'date',
            'link',
            'author',
            'glyph',
            'topic',
            'featured',
        )
