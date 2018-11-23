from rest_framework import serializers
from crumbs.models import Classroom, ClassroomBase
from .session import SessionSerializer
from .person import PersonSerializer

class ClassroomBaseSerializer(serializers.ModelSerializer):
    # school = serializers.CharField(source="school.slug", read_only=True)
    category = serializers.CharField(source="get_category_display", read_only=True)
    class Meta:
        model = ClassroomBase
        fields = "__all__"

class ClassroomSerializer(serializers.ModelSerializer):
    group_base = ClassroomBaseSerializer(read_only =True)
    session = SessionSerializer(read_only =True)
    head_teacher = PersonSerializer(read_only =True)
    className = serializers.CharField(source="name", read_only=True)
    class Meta:
        model = Classroom
        fields = "__all__"
