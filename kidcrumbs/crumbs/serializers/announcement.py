from rest_framework import serializers
from crumbs.models import Announcement
from .person import PersonSerializer


class AnnouncementSerializer(serializers.ModelSerializer):
    announcer = PersonSerializer(read_only=True)
    school = serializers.CharField(source="term.session.school.short_name", read_only = True)
    class Meta:
        model = Announcement
        fields = "__all__"
