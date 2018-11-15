from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import ActivitySerializer, ActivityItemSerializer, ActivityCommentSerializer, \
        ActivityCommentReplySerializer
from crumbs.models import Activity, ActivityItem, AdminPerson, ActivityComment, ActivityCommentReply,Person
from django.shortcuts import get_object_or_404



class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityItemViewSet(viewsets.ModelViewSet):
    queryset = ActivityItem.objects.all()
    serializer_class = ActivityItemSerializer

    def perform_create(self, serializer):
        created_by = self.request.data.pop("created_by")
        person = get_object_or_404(AdminPerson.objects,user=created_by)
        serializer.save(created_by=person)

    def update(self, request, pk=None):
        item = get_object_or_404(ActivityItem.objects,pk=pk)
        created_by = request.data.pop("created_by")
        person = get_object_or_404(AdminPerson.objects,user=created_by)
        deserialized = self.get_serializer(item, data=request.data) 
        if deserialized.is_valid():
            deserialized.save(created_by=person)
            return Response(deserialized.data)


class ActivityCommentViewSet(viewsets.ModelViewSet):
    queryset = ActivityComment.objects.all()
    serializer_class = ActivityCommentSerializer

    def perform_create(self, serializer):
        user = self.request.data.pop("person")
        person = get_object_or_404(Person.objects,user=user)
        serializer.save(person=person)



class ActivityCommentReplyViewSet(viewsets.ModelViewSet):
    queryset = ActivityCommentReply.objects.all()
    serializer_class = ActivityCommentReplySerializer

    def perform_create(self, serializer):
        user = self.request.data.pop("person")
        person = get_object_or_404(Person.objects,user=user)
        serializer.save(person=person)


