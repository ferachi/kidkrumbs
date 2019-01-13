from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import SubjectSerializer, CoreSubjectSerializer, AssessmentDetailSerializer
from crumbs.models import Subject, CoreSubject, Assessment


class CoreSubjectViewSet(viewsets.ModelViewSet):
    queryset = CoreSubject.objects.all()
    serializer_class = CoreSubjectSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @detail_route()
    def get_results(self, request, pk=None):
        """
        Gets the Subjects results
        """
        subject = self.get_object()
        results = Assessment.objects.filter(subject=subject)
        serializer = AssessmentDetailSerializer(results, many=True)
        return Response(serializer.data)


