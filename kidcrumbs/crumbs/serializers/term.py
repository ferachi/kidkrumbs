from rest_framework import serializers
from crumbs.models import Term

class TermSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(source='get_name_display')
    class Meta:
        model = Term
        fields = '__all__'
