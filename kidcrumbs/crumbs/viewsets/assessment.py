from rest_framework import viewsets
from crumbs.serializers import AssessmentSerializer,AssessmentResultSerializer, GradeSystemSerializer
from crumbs.models import Assessment,AssessmentPaper, AssessmentResult, GradeSystem
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class AssessmentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer

class GradeSystemViewSet(viewsets.ModelViewSet):
    queryset = GradeSystem.objects.all()
    serializer_class = GradeSystemSerializer
