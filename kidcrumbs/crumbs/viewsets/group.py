from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import GroupSerializer, ActivitySerializer
from crumbs.models import Group, Activity


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    @detail_route()
    def get_activities(self, request, pk=None):
        """
        Gets the Groups activities
        """
        group = self.get_object()
        activities = Activity.objects.filter(group=group)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

