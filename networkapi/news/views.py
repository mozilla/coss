from rest_framework.generics import ListAPIView, RetrieveAPIView

from networkapi.news.models import News
from networkapi.news.serializers import NewsSerializer


class NewsListView(ListAPIView):
    """
    A view that permits a GET to allow listing of News articles
    in the database
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = None


class NewsView(RetrieveAPIView):
    """
    A view that permits a GET request for a News article in the database
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
