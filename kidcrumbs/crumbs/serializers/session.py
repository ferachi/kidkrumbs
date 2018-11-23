from rest_framework import serializers
from crumbs.models import Session


class SessionSerializer(serializers.ModelSerializer):
    year = serializers.CharField(source="session_year", read_only=True)
    class Meta:
        model = Session
        fields = "__all__"
