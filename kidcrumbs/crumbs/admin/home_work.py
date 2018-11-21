from django.contrib import admin
from crumbs.models import HomeWork


@admin.register(HomeWork)
class HomeWorkAdmin(admin.ModelAdmin):
    save_as = True

