from rest_framework import serializers
from crumbs.models import Subject, CoreSubject


class CoreSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreSubject
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    core_subject = CoreSubjectSerializer(read_only=True)
    class Meta:
        model = Subject
        fields = "__all__"
