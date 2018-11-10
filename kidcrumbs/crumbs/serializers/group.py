from rest_framework import serializers
from crumbs.models import Group
from .classroom import ClassroomSerializer
from .school_group import SchoolGroupSerializer
from .membership import MembershipSerializer 

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
    

# Student group serializer
class StudentGroupSerializer(serializers.ModelSerializer):
    """ The Student group serializer is a
        the same as a group serializer but 
        brings along nested relationships in 
        classroom, schoolgroup and memberships"""

    classroom = ClassroomSerializer(read_only=True)
    schoolgroup = SchoolGroupSerializer(read_only=True)
    school = serializers.CharField(source="session.school.slug", read_only=True)

    class Meta:
        model = Group
        fields = ["id", "slug","overview","avatar", "color","session","school", 'classroom', 'schoolgroup']


