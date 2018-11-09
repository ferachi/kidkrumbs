from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import StudentSerializer, GroupSerializer, MembershipSerializer, StudentGroupSerializer
from crumbs.models import Student, Group, Membership
from crumbs.permissions import CanViewStudents


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (CanViewStudents,)
    lookup_field = 'username'

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_admin and user.is_active:
    #         return Student.objects.all
    #
    #     # check for the relationship with the current user
    #     students = Student.objects.filter(source_relations__relative__user = request.user,\
    #                 source_relations__relationship_type__in=['PT','GN'])
    #


    @detail_route()
    def get_groups(self, request, username=None):
        """
        Gets the Students' groups
        """
        student = self.get_object()
        groups = Group.objects.filter(memberships__person=student)
        serializer = StudentGroupSerializer(groups, many=True)
        return Response(serializer.data)


    @detail_route()
    def get_current_groups(self, request, username=None):
        """
        Gets the Students' groups
        """
        student = self.get_object()
        groups = Group.objects.filter(memberships__person=student, memberships__is_current = True)
        serializer = StudentGroupSerializer(groups, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_memberships(self, request, username=None):
        """
        Gets the Students' memberships to groups
        """
        student = self.get_object()
        memberships = Membership.objects.filter(person=student)
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)
