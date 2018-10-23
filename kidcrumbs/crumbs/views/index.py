from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'crumbs/crumbs_base.html'

class SplashView(TemplateView):
    template_name = "crumbs/splash_screen.html"
