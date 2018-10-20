from django.db import models
from django.utils.text import slugify
from .group import Group, AbstractGroup
from django.core.exceptions import ValidationError
from django.urls import reverse
from .user import User
import uuid


class ClassroomBase(AbstractGroup):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    short_name = models.CharField(max_length=10)
    class_wing = models.CharField(max_length=30, help_text=' gold , B')

    @property
    def full_name(self):
        return "{}-{} {}".format(self.school.short_name, self.name, self.class_wing)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Base Classrooms'


class Classroom(Group):
    classroom_base = models.ForeignKey(ClassroomBase, related_name='classrooms', on_delete=models.CASCADE)
    subjects = models.ManyToManyField("Subject", related_name='classrooms', blank=True)
    head_teacher = models.ForeignKey('Teacher', on_delete=models.DO_NOTHING, null=True, related_name='classrooms')

    @property
    def classroom_name(self):
        return "{} {}".format(self.classroom_base.name, self.classroom_base.class_wing)

    @property
    def full_name(self):
        return "{} - {}".format(self.classroom_base.full_name, self.session.session_year)
