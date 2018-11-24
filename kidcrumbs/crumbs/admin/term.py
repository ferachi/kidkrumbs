from django.contrib import admin
from crumbs.models import Term


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    save_as = True
    raw_id_fields = ('session',)
    
