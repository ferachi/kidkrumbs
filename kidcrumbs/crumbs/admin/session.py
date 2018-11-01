from django.contrib import admin
from crumbs.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    save_as = True

