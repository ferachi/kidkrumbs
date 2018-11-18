from rest_framework import serializers
from crumbs.models import Subject, CoreSubject, Syllabus, SyllabusItem, TeacherSubject
from .session import SessionSerializer
from .person import PersonSerializer

class CoreSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreSubject
        fields = "__all__"

class TeacherSubjectSerializer(serializers.ModelSerializer):
    teacher = PersonSerializer(read_only=True)
    class Meta:
        model = TeacherSubject
        fields = "__all__"

class SyllabusItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyllabusItem
        fields = "__all__"


class SyllabusSerializer(serializers.ModelSerializer):
    syllabus_items = SyllabusItemSerializer(read_only=True, many=True)
    class Meta:
        model = Syllabus
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    core_subject = CoreSubjectSerializer(read_only=True)
    syllabus = SyllabusSerializer(read_only=True)
    session = serializers.CharField(source="session.session_year",read_only=True)
    subject_teachers = TeacherSubjectSerializer(read_only=True, many=True)
    class Meta:
        model = Subject
        fields = "__all__"
