from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import RoutineSerializer, StudentRoutineSerializer
from crumbs.models import Routine, StudentRoutine


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer


class StudentRoutineViewSet(viewsets.ModelViewSet):
    queryset = StudentRoutine.objects.all()
    serializer_class = StudentRoutineSerializer


