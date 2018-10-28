from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import  account_activation_sent, activate
app_name = 'crumbsauth'

urlpatterns = [
        path('login/', auth_views.LoginView.as_view(template_name="account/login.html", redirect_field_name="/")),
        re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
        path('password_reset/',
            auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html',
                email_template_name='account/password_reset_email.html',
                subject_template_name='account/password_reset_subject.txt',
                success_url='/accounts/password_reset/done/'),
            name='password_reset'),
        path('password_reset/done/',
            auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'),
            name='password_reset_done'),
        re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html",success_url="/accounts/reset/done"), name='password_reset_confirm'),
        path('reset/done/',
            auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
            name='password_reset_complete'),
        path('account_activation_sent/', account_activation_sent, name='account_activation_sent')
        ]
