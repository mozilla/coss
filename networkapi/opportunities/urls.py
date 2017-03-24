from django.conf.urls import url

from networkapi.opportunities.views import (
    OpportunityListView,
    OpportunityView,
)

urlpatterns = [
    url('^$', OpportunityListView.as_view(), name='opportunity-list'),
    url(r'^(?P<pk>[0-9]+)/', OpportunityView.as_view(), name='opportunity'),
]
