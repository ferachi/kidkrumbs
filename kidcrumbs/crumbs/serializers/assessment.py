from rest_framework import serializers
from crumbs.models import Assessment, AssessmentType, AssessmentResult, Grade, GradeSystem
from .term import TermSerializer
from .enrollment import EnrollmentSerializer

class AssessmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentType
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    term = TermSerializer(read_only=True)
    class Meta:
        model = Assessment
        fields = '__all__'
        depth = 1


class AssessmentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentResult
        fields = '__all__'

class StudentResultSerializer(serializers.ModelSerializer):
    assessment = AssessmentSerializer(read_only=True)
    enrollment = EnrollmentSerializer(read_only=True)
    class Meta:
        model = AssessmentResult
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class GradeSystemSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True)
    class Meta:
        model = GradeSystem
        fields = '__all__'
