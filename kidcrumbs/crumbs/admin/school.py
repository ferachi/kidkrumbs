from django.contrib import admin
from crumbs.models import School, SchoolContact, SchoolFacility, SchoolService, SchoolRequirement


class SchoolServiceInline(admin.StackedInline):
    model = SchoolService

class SchoolRequirementInline(admin.StackedInline):
    model = SchoolRequirement

class SchoolContactInline(admin.StackedInline):
    model = SchoolContact

class SchoolFacilityInline(admin.StackedInline):
    model = SchoolFacility

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [ SchoolContactInline, SchoolFacilityInline, SchoolServiceInline, SchoolRequirementInline ]

