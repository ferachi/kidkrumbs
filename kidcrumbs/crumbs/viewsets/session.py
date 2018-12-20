from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from crumbs.serializers import SessionSerializer
from crumbs.models import Session



class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
