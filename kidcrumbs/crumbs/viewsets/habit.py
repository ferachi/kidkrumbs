from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import HabitSerializer, HabitOptionSerializer, HabitResponseSerializer
from crumbs.models import Habit, HabitOption, HabitResponse


class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitOptionViewSet(viewsets.ModelViewSet):
    queryset = HabitOption.objects.all()
    serializer_class = HabitOptionSerializer


class HabitResponseViewSet(viewsets.ModelViewSet):
    queryset = HabitResponse.objects.all()
    serializer_class = HabitResponseSerializer
