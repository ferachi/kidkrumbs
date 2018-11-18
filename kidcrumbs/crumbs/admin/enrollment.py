from django.contrib import admin
from crumbs.models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    save_as = True

