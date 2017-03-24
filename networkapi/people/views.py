from rest_framework.generics import ListAPIView, RetrieveAPIView

from networkapi.people.models import Person
from networkapi.people.serializers import PersonSerializer


class PeopleListView(ListAPIView):
    """
    A view that permits a GET to allow listing all the People
    in the database
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = None


class PersonView(RetrieveAPIView):
    """
    A view that permits a GET to allow listing a person
    in the database
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
