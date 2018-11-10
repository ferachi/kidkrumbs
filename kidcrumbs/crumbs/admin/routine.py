from django.contrib import admin
from crumbs.models import Routine, StudentRoutine


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(StudentRoutine)
class StudentRoutineAdmin(admin.ModelAdmin):
    save_as = True
