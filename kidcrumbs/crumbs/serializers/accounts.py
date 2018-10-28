from rest_framework import serializers
from crumbs.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','first_name','other_names','last_name','username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
