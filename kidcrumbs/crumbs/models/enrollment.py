from django.db import models
import uuid

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='enrollments')
    score = models.PositiveSmallIntegerField(blank=True, null=True) # total score of all results in this enrollment
    is_opt = models.BooleanField("optional subject?",default=False)
    is_current = models.BooleanField("currently enrolled?", default=True)
    date_enrolled = models.DateField()
    created_by = models.ForeignKey("AdminPerson", related_name='created_enrollments', on_delete=models.DO_NOTHING, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} enrollment for {1}".format(self.subject.subject_code, self.student)

    class Meta:
        unique_together = ('student','subject')
