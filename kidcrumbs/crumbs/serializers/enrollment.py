from rest_framework import serializers
from crumbs.models import Enrollment
from .subject import SubjectSerializer
from .student import StudentSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only = True)
    student = StudentSerializer(read_only = True)
    class Meta:
        model = Enrollment
        fields = "__all__"
