from django.urls import path, re_path
from crumbs import views

app_name = 'crumbs'


urlpatterns = [
        path('', views.SplashView.as_view(), name='splash'),
        path('index/', views.IndexView.as_view(), name='index'),
]
