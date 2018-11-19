from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from crumbs.utils.colors import COLORS
from crumbs.utils.image_uploaders import upload_subject_avatars_dir
import uuid


class CoreSubject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School',related_name='subjects', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,blank=True)
    overview = models.CharField(max_length=500)
    description = models.TextField()
    color = models.CharField(max_length=20, choices=COLORS, default='DODGERBLUE')
    created_by = models.ForeignKey("AdminPerson", on_delete=models.DO_NOTHING, null=True,\
            related_name="created_core_subjects")
    created_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        school = slugify(self.school.short_name)
        name = slugify(self.name)
        self.slug = '%s-%s' % (school,name)
        super(CoreSubject, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name = 'Core Subject'
        verbose_name_plural = 'Core Subjects'
        indexes = [ models.Index(fields=['name'], name='name_idx')]
        unique_together = ('name','school')


class Subject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    core_subject = models.ForeignKey('CoreSubject', verbose_name="Main Subject", related_name='subjects', on_delete=models.CASCADE)
    session = models.ForeignKey('Session',related_name='subjects',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=7)
    overview = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    avatar =  models.ImageField("school image", upload_to=upload_subject_avatars_dir, null=True, blank=True)
    color = models.CharField(max_length=20, choices=COLORS, default='#ff4500')
    created_by = models.ForeignKey("AdminPerson", on_delete=models.DO_NOTHING, null=True, related_name="created_subjects")
    created_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.name,self.subject_code)

    class Meta:
        ordering = ['subject_code']
        indexes = [models.Index(fields=['subject_code'], name='subject_code_idx')]


class Syllabus(models.Model):
    subject = models.OneToOneField(Subject, primary_key=True, on_delete=models.CASCADE, related_name='syllabus')
    description = models.TextField()
    show_duration = models.BooleanField(default=False)
    created_by = models.ForeignKey("AdminPerson", on_delete=models.DO_NOTHING, null=True,\
            related_name="created_syllabuses")
    created_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return "%s syllabus" % self.subject

    class Meta:
        verbose_name_plural = 'Syllabus'


class SyllabusItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    syllabus = models.ForeignKey(Syllabus, on_delete=models.CASCADE, related_name='syllabus_items')
    index = models.PositiveIntegerField(help_text='in sequential order as you would have it appear')
    title = models.CharField(max_length=300)
    description = models.TextField()
    duration = models.CharField(max_length=30, blank=True, help_text='e.g 3 days, 2 weeks')
    created_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now=True)

    def __str__(self):
        return self.syllabus.subject.name

    class Meta:
        ordering = ('index','title')


# intermediate model for the proxy model Teacher above and Subject
# note this has to be manually modified, as a proxy model
# can't add extra fields; in this case subject
class TeacherSubject(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey('Teacher', related_name='teacher_subjects', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', related_name='subject_teachers', blank=True, on_delete=models.CASCADE)
    created_by = models.ForeignKey("AdminPerson", on_delete=models.DO_NOTHING, null=True)
    created_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Teachers' Subjects"
        verbose_name_plural = "Teachers' Subjects"

