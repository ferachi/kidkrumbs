from django.contrib.auth import logout
from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from crumbs.serializers import AccountSerializer
from crumbs.models import User
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import status, views


# class AccountViewSet(viewsets.ModelViewSet):
# removing the ListModelMixin and CreateModelMixin by removing the ModelViewSet
# if a call to api/accounts/ is made, nothing is returned
class AccountViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'

    @list_route()
    def logout(self, request, pk=None):
        logout(request)
        return Response({'message' : 'Logged Out'}, status = status.HTTP_200_OK)
