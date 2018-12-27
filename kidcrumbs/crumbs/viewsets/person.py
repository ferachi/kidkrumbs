from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import PersonSerializer, RelationSerializer, PersonSchoolRoleSerializer, AnnouncementSerializer, SchoolSerializer
from crumbs.models import Person, Relation, PersonSchoolRole, Announcement, School
from PIL import Image
import re
import os
from io import BytesIO
import base64
from binascii import a2b_base64
import pathlib
from django.core.files.base import ContentFile
from itertools import groupby
from django.contrib.auth import authenticate, update_session_auth_hash
from crumbs.models import User


class ProfileViewSet(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @detail_route()
    def get_relationships(self, request, pk=None):
        """
        Gets the source relations
        """
        person = self.get_object()
        relations = Relation.objects.filter(person=person)
        serializer = RelationSerializer(relations, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_relatives(self, request, pk=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        serializer = PersonSerializer(person.relatives, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_schools(self, request, pk=None):
        """
        Gets the announcements from the profiles schools
        """
        person = self.get_object()
        schools = School.objects.filter(person_roles__person=person)
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)


    @detail_route()
    def get_roles(self, request, pk=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        school_roles = PersonSchoolRole.objects.filter(person=person)
        serializer = PersonSchoolRoleSerializer(school_roles, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_announcements(self, request, pk=None):
        """
        Gets the announcements from the persons schools
        """
        person = self.get_object()
        announcements = Announcement.objects.filter(term__session__school__person_roles__person=person)
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'username'

    @detail_route()
    def get_relationships(self, request, username=None):
        """
        Gets the source relations
        """
        person = self.get_object()
        relations = Relation.objects.filter(person=person)
        serializer = RelationSerializer(relations, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_relatives(self, request, username=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        serializer = PersonSerializer(person.relatives, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_roles(self, request, username=None):
        """
        Gets the persons relatives
        """
        person = self.get_object()
        school_roles = PersonSchoolRole.objects.filter(person=person)
        serializer = PersonSchoolRoleSerializer(school_roles, many=True)
        return Response(serializer.data)

    @detail_route(methods=["put"])
    def update_avatar(self, request, username=None):
        person = self.get_object()
        # remove the image from the user object; this was an added attribute
        image_uri = request.data.pop('image')

        # deserialize the request data
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            if image_uri:
                imgstr = re.search(r'(\w*;)(base64,)(.*)', image_uri)
                file_name = "%s.%s" % (person.full_name, imgstr.group(1)[:-1])
                person.avatar = ContentFile(base64.b64decode(imgstr.group(3)), file_name)
                person = person.save()
                serializer = PersonSerializer(person)
                return Response({'message': 'user updated', 'profile':serializer.data},status=status.HTTP_200_OK)
        return Response({'message': 'invalid data', 'errors':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=["put"])
    def update_profile(self, request, username=None):
        person = self.get_object()
        # remove the image from the user object; this was an added attribute
        username = request.data.pop('_username')

        # if this request was done by the same user
        if request.user.id == person.user.id:
            serializer = PersonSerializer(person, data=request.data)

            # is it valid; then save
            if serializer.is_valid():

                serializer.save()

                # is there a change in the username
                if username != request.user.username:
                    user = User.objects.get(id=request.user.id)
                    user.username = username
                    user.save()

                    # update serializer
                    person = Person.objects.get(user=user)
                    serializer = PersonSerializer(person)

                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'invalid':True}, status=status.HTTP_401_UNAUTHORIZED) 

    @list_route(methods=["post"])
    def check_username(self, request):
        username = request.data.pop('newUsername')
        userId = request.data.pop('user')


        if str(request.user.id) == userId:
            if request.user.username != username:
                try:
                    User.objects.get(username = username)
                    return Response({'valid':False,'message': 'username already exist'},status=status.HTTP_200_OK)
                except User.DoesNotExist: 
                    return Response({'valid':True,'message': 'Username Ok'},status=status.HTTP_200_OK)
            
            return Response({'valid':True,'message': 'Username Ok'},status=status.HTTP_200_OK)
        return Response({'valid': False, 'message':"ILLEGAL ENTRY"},status=status.HTTP_400_BAD_REQUEST)


    @list_route(methods=["post"])
    def change_password(self, request):
        password = request.data.pop('password')
        userId = request.data.pop('user')

        if str(request.user.id) == userId:
            user = User.objects.get(id=userId)
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
            return Response({'valid':True,'message': 'user updated'},status=status.HTTP_200_OK)
        return Response({'message': "You can't update another user"},status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=['post'])
    def validate_password(self, request):
        password = request.data.pop('password')
        userId = request.data.pop('user')

        if str(request.user.id) == userId:
            user = authenticate(username=request.user.username, password=password)
            if user:
                return Response({'valid': True, 'message':"Password Ok"},status=status.HTTP_200_OK)
            return Response({'valid': False, 'message':"Wrong Password"},status=status.HTTP_200_OK)
        return Response({'valid': False, 'message':"ILLEGAL ENTRY"},status=status.HTTP_400_BAD_REQUEST)
        

# class ValidateViewset(viewse.ViewSet):
#     @detail_route(methods=["post"])
#     def change_password(self, request, username=None):
#         person = self.get_object()
#         password = request.data.pop('password')
#
#         if user.id == person.user.id:
#             user.set_password(password)
#             user.save()
#             serializer = PersonSerializer(person)
#             return Response({'message': 'user updated', 'profile':serializer.data},status=status.HTTP_200_OK)
#         return Response({'message': "You can't update another user"},status=status.HTTP_400_BAD_REQUEST)
#
#     @detail_route(methods=["post"])
#     def validate_password(self, request, username=None):
#         person = self.get_object()
#         password = request.data.pop('password')
#
#         # deserialize the request data
#         user = authenticate(username=person.username, password=password)
#         if user:
#             return Response({'valid': True, 'message':"Password Ok"},status=status.HTTP_200_OK)
#         return Response({'valid': False, 'message':"Wrong Password"},status=status.HTTP_200_OK)
        



