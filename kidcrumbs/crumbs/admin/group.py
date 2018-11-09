from django.contrib import admin
from crumbs.models import Group, Classroom, ClassroomBase, SchoolGroup, SchoolGroupBase


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(ClassroomBase)
class ClassroomBaseAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(SchoolGroup)
class SchoolGroupAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(SchoolGroupBase)
class SchoolGroupBaseAdmin(admin.ModelAdmin):
    save_as = True

