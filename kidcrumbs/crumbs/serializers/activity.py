from rest_framework import serializers
from crumbs.models import Activity, ActivityItem,ActivityComment, ActivityCommentReply
from .person import PersonSerializer

class ActivityItemSerializer(serializers.ModelSerializer):
    created_by = PersonSerializer(read_only=True)
    class Meta:
        model = ActivityItem
        fields = ['id','title','description','color','created_date','time','created_by', 'activity']


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.color = validated_data.get('color', instance.color)
        instance.time = validated_data.get('time', instance.time)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.save()
        return instance

class ActivityCommentReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCommentReply
        fields = "__all__"
        depth = 1

class ActivityCommentSerializer(serializers.ModelSerializer):
    replies = ActivityCommentReplySerializer(many=True, read_only=True)
    class Meta:
        model = ActivityComment
        fields = "__all__"
        depth = 1

class ActivitySerializer(serializers.ModelSerializer):
    activities = ActivityItemSerializer(many=True, read_only=True)
    comments = ActivityCommentSerializer(many=True, read_only=True)
    school = serializers.CharField(source="group.session.school.slug", read_only=True)
    class Meta:
        model = Activity
        fields = ['id','group','note', 'color','school', 'created_by', 'date', 'activities', 'comments']


