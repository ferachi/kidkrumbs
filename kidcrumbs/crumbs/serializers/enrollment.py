from rest_framework import serializers
from crumbs.models import Enrollment
from .subject import SubjectSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only = True)
    class Meta:
        model = Enrollment
        fields = "__all__"
