from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import PersonSerializer, RelationSerializer, PersonSchoolRoleSerializer, AnnouncementSerializer, SchoolSerializer
from crumbs.models import Person, Relation, PersonSchoolRole, Announcement, School


class ProfileViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
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
    def get_schools(self, request, pk=None):
        """
        Gets the announcements from the profiles schools
        """
        person = self.get_object()
        schools = School.objects.filter(person_roles__person=person)
        serializer = SchoolSerializer(schools, many=True)
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

    @detail_route()
    def get_announcements(self, request, pk=None):
        """
        Gets the announcements from the persons schools
        """
        person = self.get_object()
        announcements = Announcement.objects.filter(term__session__school__person_roles__person=person)
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)

class PersonViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'username'

    @detail_route()
    def get_relationships(self, request, username=None):
        """
        Gets the source relations
        """
        person = self.get_object()
        relations = Relation.objects.filter(person=person)
        serializer = RelationSerializer(relations, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_relatives(self, request, username=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        serializer = PersonSerializer(person.relatives, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_roles(self, request, username=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        school_roles = PersonSchoolRole.objects.filter(person=person)
        serializer = PersonSchoolRoleSerializer(school_roles, many=True)
        return Response(serializer.data)
