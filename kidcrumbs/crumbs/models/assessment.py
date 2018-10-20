from django.db import models
from django.utils.text import slugify
from crumbs.utils.image_uploaders import upload_assessment, upload_assessment_results
from crumbs.utils.colors import COLORS
import uuid


class AssessmentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30 , unique=True)
    color = models.CharField(max_length=20, choices=COLORS)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="assessment_types")
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Assessment Types'


class AssessmentResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    enrollment = models.ForeignKey('Enrollment', on_delete=models.CASCADE, related_name='assessment_results')
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, related_name='assessment_results')
    date_taken = models.DateField()
    score = models.PositiveSmallIntegerField()
    hard_copy = models.ImageField("Scanned Result", upload_to=upload_assessment_results, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{0} result for {1}".format(self.assessment, self.enrollment.student.full_name )

    class Meta:
        permissions = ( ('view_all_assessmentresult', 'Can view all assessment result'),)
        verbose_name_plural = 'Assessment Results'


class Assessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='assessments')
    assessment_type = models.ForeignKey('AssessmentType', on_delete=models.CASCADE, related_name='assessments')
    term = models.ForeignKey('Term', on_delete=models.CASCADE, related_name='assessments')
    description = models.TextField()
    max_score = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.subject.subject_code, self.assessment_type.name)

    class Meta:
        ordering = ['max_score']
        permissions = ( ('view_student_assessment', 'Can view assessment'),)

class AssessmentPaper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    overview = models.TextField(blank=True)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='papers')
    classroom = models.ForeignKey('ClassRoom', on_delete=models.CASCADE, related_name='papers')
    hard_copy = models.FileField("Scanned Assessment", upload_to=upload_assessment, help_text="jpg, png, doc, pdf")
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Assessment Papers'
        unique_together = ('classroom','assessment')



class GradeSystem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150)
    overview = models.TextField()
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name="grade_systems")
    is_current= models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Grading System'



class Grade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    grade_system = models.ForeignKey(GradeSystem, on_delete=models.CASCADE, related_name="grades")
    grade_char = models.CharField("Grade Letter", max_length=1,unique=True, help_text="A, B,...,E, F")
    min_value = models.PositiveSmallIntegerField()
    max_value = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20, choices=COLORS)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.grade_char

    class Meta:
        ordering = ['grade_char']
