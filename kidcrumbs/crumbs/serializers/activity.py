from rest_framework import serializers
from crumbs.models import Activity, ActivityItem

class ActivityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityItem
        fields = "__all__"

class ActivitySerializer(serializers.ModelSerializer):
    activities = ActivityItemSerializer(many=True)
    class Meta:
        model = Activity
        fields = ['group','note', 'color', 'created_by', 'date', 'activities']
