from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import StudentSerializer
from crumbs.models import Student
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
