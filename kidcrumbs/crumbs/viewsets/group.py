from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import GroupSerializer, ActivitySerializer, PersonSerializer, RoutineSerializer, HabitSerializer
from crumbs.models import Group, Activity, Membership, Person, Routine, Habit


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


    @detail_route()
    def get_current_members(self, request, pk=None):
        """
        Gets the Groups current members
        """
        group = self.get_object()
        # current members only
        members = Person.objects.filter(memberships__group=group, memberships__is_current=True)
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_current_students(self, request, pk=None):
        """
        Gets the Groups current students
        """
        group = self.get_object()
        # current members only
        members = Person.objects.filter(memberships__group=group, memberships__is_current=True,\
        person_school_roles__roles__name='student')
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_current_teachers(self, request, pk=None):
        """
        Gets the Groups current teachers
        """
        group = self.get_object()
        # current members only
        members = Person.objects.filter(memberships__group=group, memberships__is_current=True,\
        person_school_roles__roles__name='teacher')
        serializer = PersonSerializer(members, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_routines(self, request, pk=None):
        """
        Gets the Groups Routines
        """
        group = self.get_object()
        routines = Routine.objects.filter(group=group)
        serializer = RoutineSerializer(routines, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_habits(self, request, pk=None):
        """
        Gets the Groups Routines
        """
        group = self.get_object()
        habits = Habit.objects.filter(groups=group)
        serializer = HabitSerializer(habits, many=True)
        return Response(serializer.data)
