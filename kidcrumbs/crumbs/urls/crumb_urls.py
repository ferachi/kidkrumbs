from django.urls import path
from crumbs import views

app_name = 'crumbs'


urlpatterns = [
        path('', views.IndexView.as_view(), name='idex'),
]
