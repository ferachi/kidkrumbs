from django.db import models


class AdminPersonManager(models.Manager):
    def get_queryset(self):
        return super(AdminPersonManager, self).get_queryset().filter(person_roles__roles__name='administrator')

class SuperAdminPersonManager(models.Manager):
    def get_queryset(self):
        return super(SuperAdminPersonManager, self).get_queryset().filter(person_roles__roles__name='super administrator')

class OtherAdminPersonManager(models.Manager):
    def get_queryset(self):
        return super(OtherAdminPersonManager, self).get_queryset().filter(person_roles__roles__name='other administrator')

class ExternalPersonManager(models.Manager):
    def get_queryset(self):
        return super(SchoolPersonManager, self).get_queryset().filter(person_roles__roles__name='external')


class NonAdminPersonManager(models.Manager):
    def get_queryset(self):
        return super(NonAdminPersonManager, self).get_queryset().filter(person_roles__roles__name='non administrator')


class RelativeManager(models.Manager):
    def get_queryset(self):
        return super(RelativeManager, self).get_queryset().filter(person_roles__roles__name='relative')


class SchoolPersonManager(models.Manager):
    def get_queryset(self):
        return super(SchoolPersonManager, self).get_queryset().filter(person_roles__roles__name='school')


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(person_roles__roles__name='student')


class TeacherManager(models.Manager):
    def get_queryset(self):
        return super(TeacherManager, self).get_queryset().filter(person_roles__roles__name='teacher')


class HeadTeacherManager(models.Manager):
    def get_queryset(self):
        return super(HeadTeacherManager, self).get_queryset().filter(person_roles__roles__name='head teacher')
