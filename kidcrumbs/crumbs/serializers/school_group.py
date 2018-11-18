from rest_framework import serializers
from crumbs.models import SchoolGroup


class SchoolGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolGroup
        fields = "__all__"
