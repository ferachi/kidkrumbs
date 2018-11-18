from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import SubjectSerializer, CoreSubjectSerializer
from crumbs.models import Subject, CoreSubject


class CoreSubjectViewSet(viewsets.ModelViewSet):
    queryset = CoreSubject.objects.all()
    serializer_class = CoreSubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

