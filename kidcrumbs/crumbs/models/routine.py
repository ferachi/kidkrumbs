from django.db import models
import uuid


class Routine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="routines")
    date = models.DateField()
    comment = models.TextField()
    message = models.TextField("message/request")
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

