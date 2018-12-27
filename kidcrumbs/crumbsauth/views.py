from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.db.models import Q

from django.conf import settings
from crumbs.models import User


from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from rest_framework import status, views
from rest_framework.response import Response


# from .serializers import AccountSerializer
from .tokens import account_activation_token

def activate(request, uidb64, token):
    '''
        Activate
        Called when the user clicks the link on the email
        Used to activate the user
    '''
    try:
        uid = force_text(urlsafe_base64_decode(uidb64.encode()))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.person.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('knobapp:home')
    else:
        return render(request, 'account/account_activation_invalid.html')

def account_activation_sent(request):
    return render(request,'account/account_activation_sent.html')

class TokenView(views.APIView):
    def get(self, request,format=None):
        return_obj = {'csrftoken':request.COOKIES.get('csrftoken'),'session':request.COOKIES.get('sessionid'), 'user':request.user.id, 'authenticated':request.user.is_authenticated}
        return Response(return_obj)


class LogoutView(views.APIView):
    def get(self, request, format=None):
        logout(request)
        return Response({'message' : 'Logged Out'}, status = status.HTTP_200_OK)
