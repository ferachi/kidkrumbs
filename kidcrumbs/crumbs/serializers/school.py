from rest_framework import serializers
from crumbs.models import School, SchoolFacility, SchoolRequirement, SchoolService, SchoolContact



class SchoolFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolFacility
        fields = "__all__"

class SchoolServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolService
        fields = "__all__"

class SchoolRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolRequirement
        fields = "__all__"

class SchoolContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolContact
        fields = "__all__"

class SchoolSerializer(serializers.ModelSerializer):
    requirements = SchoolRequirementSerializer(read_only=True, many=True)
    services = SchoolServiceSerializer(read_only=True, many=True)
    facilities = SchoolFacilitySerializer(read_only=True, many=True)
    contact = SchoolContactSerializer(read_only=True)

    class Meta:
        model = School
        fields = "__all__"
