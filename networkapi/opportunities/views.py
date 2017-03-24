from rest_framework.generics import ListAPIView, RetrieveAPIView

from networkapi.opportunities.models import Opportunity
from networkapi.opportunities.serializers import OpportunitySerializer


class OpportunityListView(ListAPIView):
    """
    A view that permits a GET to allow listing of Opportunities
    in the database
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
    pagination_class = None


class OpportunityView(RetrieveAPIView):
    """
    A view that permits a GET request for an Opportunity in the database
    """
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer
