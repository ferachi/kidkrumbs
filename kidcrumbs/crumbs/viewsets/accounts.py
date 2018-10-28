from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from crumbs.serializers import AccountSerializer
from crumbs.models import User


# class AccountViewSet(viewsets.ModelViewSet):
# removing the ListModelMixin and CreateModelMixin by removing the ModelViewSet
# if a call to api/accounts/ is made, nothing is returned
class AccountViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'id'

