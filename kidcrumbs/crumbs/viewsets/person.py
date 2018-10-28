from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import PersonSerializer, RelationSerializer, PersonSchoolRoleSerializer
from crumbs.models import Person, Relation, PersonSchoolRole


# class AccountViewSet(viewsets.ModelViewSet):
# removing the ListModelMixin and CreateModelMixin by removing the ModelViewSet
# if a call to api/accounts/ is made, nothing is returned
class PersonViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @detail_route()
    def get_relationships(self, request, pk=None):
        """
        Gets the source relations
        """
        person = self.get_object()
        relations = Relation.objects.filter(person=person)
        serializer = RelationSerializer(relations, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_relatives(self, request, pk=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        serializer = PersonSerializer(person.relatives, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_roles(self, request, pk=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        school_roles = PersonSchoolRole.objects.filter(person=person)
        serializer = PersonSchoolRoleSerializer(school_roles, many=True)
        return Response(serializer.data)
