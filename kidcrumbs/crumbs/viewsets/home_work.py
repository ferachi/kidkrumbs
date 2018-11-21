from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import HomeWorkSerializer
from crumbs.models import HomeWork, Subject, AdminPerson,Teacher
from django.shortcuts import get_object_or_404

class HomeWorkViewSet(viewsets.ModelViewSet):
    queryset = HomeWork.objects.all()
    serializer_class = HomeWorkSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        subjectId = request.data.get('subject')
        teacherId = request.data.get('teacher')
        user = request.user
        subject = get_object_or_404(Subject, pk=subjectId)
        admin_person = get_object_or_404(AdminPerson, pk=user.id)
        teacher = get_object_or_404(Teacher, pk=user.id)
        serializer.is_valid(raise_exception=True)
        serializer.save(subject=subject, created_by=admin_person, teacher=teacher)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        homework = self.get_object()
        serializer = self.get_serializer(homework,data=request.data)
        subjectId = request.data.get('subject')
        teacherId = request.data.get('teacher')
        user = request.user
        subject = get_object_or_404(Subject, pk=subjectId)
        admin_person = get_object_or_404(AdminPerson, pk=user.id)
        teacher = get_object_or_404(Teacher, pk=user.id)
        serializer.is_valid(raise_exception=True)
        serializer.save(subject=subject, created_by=admin_person, teacher=teacher)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED, headers=headers)
        

