from django.contrib import admin
from crumbs.models import School, SchoolContact


class SchoolContactInline(admin.StackedInline):
    model = SchoolContact

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [ SchoolContactInline ]

