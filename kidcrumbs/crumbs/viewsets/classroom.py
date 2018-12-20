from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import ClassroomSerializer, ActivitySerializer, SubjectSerializer,\
HomeWorkSerializer,PersonSerializer
from crumbs.models import Classroom, Activity, Subject, HomeWork, Person


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    @detail_route()
    def get_subjects(self, request, pk=None):
        """
        Gets the classrooms' subjects
        """
        classroom = self.get_object()
        subjects = Subject.objects.filter(classrooms=classroom)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_homeworks(self, request, pk=None):
        """
        Gets the Classrooms' Homework
        """
        classroom = self.get_object()
        homeworks = HomeWork.objects.filter(classroom=classroom)
        serializer = HomeWorkSerializer(homeworks, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_members(self, request, pk=None):
        """
        Gets the Classrooms' members
        """
        classroom = self.get_object()
        members = Person.objects.filter(group_list=classroom)
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)
