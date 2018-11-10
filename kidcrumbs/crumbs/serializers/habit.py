from rest_framework import serializers
from crumbs.models import Habit, HabitOption, HabitResponse


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"


class HabitOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitOption
        fields = "__all__"


class HabitResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitResponse
        fields = "__all__"

