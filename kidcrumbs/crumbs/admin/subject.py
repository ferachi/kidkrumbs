from django.contrib import admin
from crumbs.models import Subject, CoreSubject, Syllabus, SyllabusItem


class SyllabusItemInline(admin.StackedInline):
    model = SyllabusItem


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(CoreSubject)
class CoreSubjectAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [ SyllabusItemInline ]

