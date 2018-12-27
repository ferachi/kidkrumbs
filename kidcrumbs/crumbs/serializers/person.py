from rest_framework import serializers
from crumbs.models import Person, Relation, PersonSchoolRole,PersonContact, MedicalInformation


class PersonContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonContact
        fields = '__all__'


class MedicalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInformation
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    id  = serializers.CharField(source="user.pk", read_only=True)
    first_name  = serializers.CharField(source="user.first_name", read_only=True)
    last_name  = serializers.CharField(source="user.last_name", read_only=True)
    other_names  = serializers.CharField(source="user.other_names", read_only=True)
    username  = serializers.CharField(read_only=True)
    email  = serializers.CharField(source="user.email", read_only=True)
    names = serializers.CharField(source="full_name", read_only=True)
    contact = PersonContactSerializer(read_only=True)
    medical_info = MedicalInformationSerializer(read_only=True)

    class Meta:
        model = Person
        fields = [ "user", "first_name","last_name","other_names","names", "username","avatar", "email", "title", "description","occupation",
                "gender", "dob", "hobbies", "qualifications", "id", "contact", "medical_info"]
        extra_kwargs = {'avatar': {'read_only': True}}


class RelationSerializer(serializers.ModelSerializer):
    relationship_type_display = serializers.CharField(source="get_relationship_type_display")
    class Meta:
        model = Relation
        fields = ['relationship_type_display', 'relationship', 'relationship_type', 'relative'] 


class PersonSchoolRoleSerializer(serializers.ModelSerializer):
    roles = serializers.StringRelatedField(many=True)
    school = serializers.CharField(source="school.slug")
    username = serializers.CharField(source="person.user.username")
    class Meta:
        model = PersonSchoolRole
        fields = ["username", "school", "roles"]
