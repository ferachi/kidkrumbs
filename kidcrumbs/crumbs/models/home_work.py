from django.db import models
import uuid


class HomeWork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.ForeignKey("Subject", on_delete=models.CASCADE, related_name="assignments")
    overview = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    teacher = models.ForeignKey("Teacher", null=True, on_delete=models.DO_NOTHING, related_name="assigned_home_works")
    created_by = models.ForeignKey("AdminPerson", null=True, on_delete=models.DO_NOTHING, \
    related_name="created_home_works")
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} home work".format(self.subject)

