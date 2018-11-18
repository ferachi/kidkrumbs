from rest_framework import serializers
from crumbs.models import Routine, StudentRoutine
from .habit import HabitResponseSerializer


class RoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"


class StudentRoutineListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        student_routines = [StudentRoutine(**item) for item in validated_data]
        return StudentRoutine.objects.bulk_create(student_routines)


class StudentRoutineSerializer(serializers.ModelSerializer):
    routine = RoutineSerializer(read_only=True)
    attitudes = HabitResponseSerializer(many=True, read_only=True)
    class Meta:
        list_serializer_class = StudentRoutineListSerializer
        model = StudentRoutine
        fields = "__all__"
    
