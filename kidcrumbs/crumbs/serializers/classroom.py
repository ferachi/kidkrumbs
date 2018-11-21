from rest_framework import serializers
from crumbs.models import Classroom, ClassroomBase
from .session import SessionSerializer

class ClassroomBaseSerializer(serializers.ModelSerializer):
    # school = serializers.CharField(source="school.slug", read_only=True)
    class Meta:
        model = ClassroomBase
        fields = "__all__"

class ClassroomSerializer(serializers.ModelSerializer):
    group_base = ClassroomBaseSerializer(read_only =True)
    session = SessionSerializer(read_only =True)
    class Meta:
        model = Classroom
        fields = "__all__"
