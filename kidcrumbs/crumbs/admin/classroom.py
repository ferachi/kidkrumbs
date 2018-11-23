from django.contrib import admin
from crumbs.models import Classroom, ClassroomBase, Enrollment
from crumbs.utils.image_editor import crop_image
from .group import GroupAdmin
from datetime import date

@admin.register(ClassroomBase)
class ClassroomBaseAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['name', 'class_wing', 'school']

@admin.register(Classroom)
class ClassroomAdmin(GroupAdmin):
    exclude = ('name',)
    raw_id_fields = ('group_base',)

    def save_model(self, request, object, form, change):
        # select all the student members of this classroom
        students = object.members.filter(person_school_roles__roles__name="student")

        classroom_subjects = object.subjects.all()
        new_subjects = form.cleaned_data.get('subjects')
        
        deleted_subjects = set(classroom_subjects) - set(new_subjects)

        for student in students:
            for subject in list(deleted_subjects):
                try:
                    enrollment = Enrollment.objects.get(student=student, subject=subject)
                    enrollment.delete()
                except Enrollment.DoesNotExist:
                    pass

            for subject in new_subjects:
                enrollment = Enrollment.objects.update_or_create(student=student, subject=subject, date_enrolled=date.today())


        # student, subject and date
        # for student in students:
        #     enrollment = Enrollment.objects.update_or_create(student=student, subject=cs3)
        #     if not enrollment.exists():
        #         print('no enrollment exist create them')
        #         Enrollment.objects.create(student=student, subject=cs3, date_enrolled=date.today())

        super(ClassroomAdmin, self).save_model(request,object,form,change)

