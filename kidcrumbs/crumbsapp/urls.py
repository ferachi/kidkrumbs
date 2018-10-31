from django.conf.urls import url, include
from .views import AppView
from crumbsauth.views import TokenView 
from crumbs.viewsets import *

from rest_framework.routers import DefaultRouter

app_name = 'crumbsapp'

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'people', PersonViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    url(r'^$', AppView.as_view(), name='home'),
    url(r'^token/$', TokenView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^.*/$',AppView.as_view(),name='any_other')
]
