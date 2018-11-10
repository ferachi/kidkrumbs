from rest_framework import serializers
from crumbs.models import Routine, StudentRoutine


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"


class StudentRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRoutine
        fields = "__all__"
