from rest_framework import viewsets, status
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

class StudentResultViewSet(viewsets.ModelViewSet):
    queryset = AssessmentResult.objects.all()
    serializer_class = AssessmentResultSerializer

    def create(self, request, *args, **kwargs):
        # USING A CREATE TO DO BOTH UPDATE AND CREATION OF RESULTS
        # THIS IS BECAUSE I CANT FIND A WAY TO UPDATE A LIST OF ITEMS
        # VIA A REST PUT METHOD AS A PUT METHOD REQUIRES AN ID/KEY 

        # the data is a list of results
        data = request.data
        
        # some of these results have id's (updates) and others don't have (creates)

        #create list for updates and new results
        updates = []
        creates = []

        # seperate data into the list w.r.t id
        for datum in data:
            _datum = datum.get('id', None) 
            if _datum is None:
                creates.append(datum)
            else:
                updates.append(datum)

        # get the existing instances for updates
        # first map out the ids
        ids = list(map(lambda x : x['id'], updates))
        
        # get the instances
        instances = self.get_queryset().filter(id__in=ids)
        
        serializer = self.get_serializer(instances, data=data, many=isinstance(data,list))
        serializer.is_valid()
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

