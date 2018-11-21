from rest_framework import serializers
from crumbs.models import HomeWork, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']


class HomeWorkSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    teacher = serializers.CharField(read_only=True, source="teacher.full_name")
    class Meta:
        model = HomeWork
        fields = "__all__"
