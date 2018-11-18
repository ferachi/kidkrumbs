from django.contrib import admin
from crumbs.models import Group, Classroom, ClassroomBase


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    save_as = True

