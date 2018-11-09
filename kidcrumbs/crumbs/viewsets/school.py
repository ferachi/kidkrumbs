from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import SchoolSerializer, GroupSerializer
from crumbs.models import School, Group


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @detail_route()
    def get_groups(self, request, pk=None):
        """
        Gets the Schools' groups
        """
        school = self.get_object()
        groups = Group.objects.filter(session__school=school)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
