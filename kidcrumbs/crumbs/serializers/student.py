from rest_framework import serializers
from crumbs.models import Student
from .person import PersonContactSerializer, MedicalInformationSerializer


class StudentSerializer(serializers.ModelSerializer):
    id  = serializers.CharField(source="user.pk", read_only=True)
    first_name  = serializers.CharField(source="user.first_name", read_only=True)
    last_name  = serializers.CharField(source="user.last_name", read_only=True)
    other_names  = serializers.CharField(source="user.other_names", read_only=True)
    username  = serializers.CharField(read_only=True)
    email  = serializers.CharField(source="user.email", read_only=True)
    names = serializers.CharField(source="full_name", read_only=True)
    gender = serializers.CharField(source="get_gender_display", read_only=True)
    contact = PersonContactSerializer(read_only = True)
    medical_info = MedicalInformationSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [ "user", "first_name","last_name","other_names","names", "username","avatar", "email", "title", "description","occupation",
                "gender", "dob", "hobbies", "qualifications", "id", "contact", "medical_info" ]

