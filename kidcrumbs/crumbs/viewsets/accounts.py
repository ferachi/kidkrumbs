from django.contrib.auth import logout, authenticate, login
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
    def logout(self, request):
        logout(request)
        return Response({'message' : 'Logged Out'}, status = status.HTTP_200_OK)

    @list_route(methods=["post"])
    def login_user(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = AccountSerializer(user)
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response({'valid':False}, status=status.HTTP_401_UNAUTHORIZED) 
