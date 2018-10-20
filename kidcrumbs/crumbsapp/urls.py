from django.conf.urls import url, include
from .views import AppView

from rest_framework.routers import DefaultRouter

app_name = 'crumbsapp'

router = DefaultRouter()

urlpatterns = [
    url(r'^$', AppView.as_view(), name='home'),
    # url(r'^api/', include(router.urls)),
    url(r'^.*/$',AppView.as_view(),name='any_other')
]
