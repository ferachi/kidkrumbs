from rest_framework import serializers
from crumbs.models import Term
from .session import SessionSerializer

class TermSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(source='get_name_display')
    session = SessionSerializer(read_only=True)
    class Meta:
        model = Term
        fields = '__all__'
