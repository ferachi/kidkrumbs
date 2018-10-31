from django.apps import AppConfig


class CrumbsConfig(AppConfig):
    name = 'crumbs'
    
    def ready(self):
    	import crumbs.signals
