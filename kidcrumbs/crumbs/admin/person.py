from django.contrib import admin
from crumbs.models import Person, Role, PersonSchoolRole, Relation, Student, ExternalPerson,\
PersonContact,MedicalInformation


class PersonContactInline(admin.StackedInline):
    model = PersonContact

class MedicalInformationInline(admin.StackedInline):
    model = MedicalInformation

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name']
    search_fields = ['^user__first_name', '^user__last_name']
    save_as = True
    inlines = [ PersonContactInline, MedicalInformationInline ]

    def first_name(self, obj):
            return obj.user.first_name
    first_name.admin_order_field = 'user__first_name'
    first_name.short_description = 'first name'

    def last_name(self, obj):
            return obj.user.first_name
    last_name.admin_order_field = 'user__last_name'
    last_name.short_description = 'last name'

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(PersonSchoolRole)
class PersonSchoolRoleAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(Relation)
class RelationAdmin(admin.ModelAdmin):
    save_as = True


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    save_as = True

@admin.register(ExternalPerson)
class ExternalPersonAdmin(admin.ModelAdmin):
    save_as = True
