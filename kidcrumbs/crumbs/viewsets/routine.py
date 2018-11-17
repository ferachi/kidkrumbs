from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import RoutineSerializer, StudentRoutineSerializer, HabitResponseSerializer
from crumbs.models import Routine, StudentRoutine, HabitResponse


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer

    @detail_route()
    def get_students_routines(self, request, pk=None):
        """
        Gets the Routines students routines
        """
        routine = self.get_object()
        # current members only
        student_routines = StudentRoutine.objects.filter(routine=routine)
        serializer = StudentRoutineSerializer(student_routines, many=True)
        return Response(serializer.data)

class StudentRoutineViewSet(viewsets.ModelViewSet):
    queryset = StudentRoutine.objects.all()
    serializer_class = StudentRoutineSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data, many=isinstance(data,list))
        serializer.is_valid(raise_exception=True)
        if isinstance(data, list):
            routineId = data[0].get('routine')
        else:
            routineId = data.get('routine')
        routine = Routine.objects.get(id=routineId)
        serializer.save(routine=routine)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, pk=None):
        routine = self.get_object()
        serializer = self.get_serializer(routine,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        attitudes = HabitResponse.objects.filter(student_routine=routine)
        responses = HabitResponseSerializer(attitudes, data=request.data.get('attitudes'), many=True)
        responses.is_valid()
        responses.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @detail_route()
    def get_students_attitudes(self, request, pk=None):
        """
        Gets the Routines students attitudes
        """
        routine = self.get_object()
        # current members only
        student_attitudes = HabitResponse.objects.filter(student_routine=routine)
        serializer = HabitResponseSerializer(student_attitudes, many=True)
        return Response(serializer.data)


