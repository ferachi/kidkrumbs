from rest_framework import serializers
from crumbs.models import Assessment, AssessmentType, AssessmentResult, Grade, GradeSystem
from .term import TermSerializer
from .enrollment import EnrollmentSerializer

class AssessmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssessmentType
        fields = '__all__'


class AssessmentSerializer(serializers.ModelSerializer):
    term = TermSerializer(read_only=True)
    class Meta:
        model = Assessment
        fields = '__all__'
        depth = 1

class AssessmentResultListSerializer(serializers.ListSerializer):
    # def create(self, validated_data):
    #     assessment_results = [AssessmentResult(**item) for item in validated_data]
    #     return AssessmentResult.objects.bulk_create(assessment_results)

    def update(self, instances, validated_data):
        response_mapping = {str(response.id): response for response in instances}
        data_mapping = [ item for item in validated_data]


        data = []
        for response in data_mapping:
            id = response.get('id', None)
            if id is None:
                data.append(self.child.create(response))
            else:
                instance = response_mapping[id]
                data.append(self.child.update(instance, response))

        # for response_id, _response in response_mapping.items():
        #     if response_id not in data_mapping:
        #         response.delete()

        return data
        


class AssessmentResultSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    class Meta:
        list_serializer_class = AssessmentResultListSerializer
        model = AssessmentResult
        fields = '__all__'

class AssessmentDetailSerializer(serializers.ModelSerializer):
    term = TermSerializer(read_only=True)
    assessment_results = AssessmentResultSerializer(many=True, read_only = True)
    class Meta:
        model = Assessment
        fields = '__all__'
        depth = 1


class StudentResultSerializer(serializers.ModelSerializer):
    assessment = AssessmentSerializer(read_only=True)
    enrollment = EnrollmentSerializer(read_only=True)
    class Meta:
        model = AssessmentResult
        fields = '__all__'

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class GradeSystemSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True)
    class Meta:
        model = GradeSystem
        fields = '__all__'
