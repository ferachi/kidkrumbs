from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import ClassroomSerializer, ActivitySerializer, SubjectSerializer
from crumbs.models import Classroom, Activity, Subject


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

