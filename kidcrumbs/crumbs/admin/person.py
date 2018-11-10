from django.contrib import admin
from crumbs.models import Person, Role, PersonSchoolRole, Relation, Student

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    save_as = True

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

