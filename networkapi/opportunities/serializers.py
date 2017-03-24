from rest_framework import serializers

from networkapi.opportunities.models import Opportunity


class OpportunitySerializer(serializers.ModelSerializer):
    """
    Serializes an Opportunity Model
    """
    link = serializers.SerializerMethodField()

    def get_link(self, opportunity):
        return {
            'label': opportunity.link_label,
            'url': opportunity.link_url,
        }

    class Meta:
        model = Opportunity
        fields = (
            'name',
            'description',
            'link',
            'featured',
            'image'
        )
