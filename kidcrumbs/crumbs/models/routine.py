from django.db import models
import uuid


class Routine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey("Group", on_delete=models.CASCADE, related_name="routines")
    date = models.DateField()
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('AdminPerson', on_delete=models.DO_NOTHING, related_name='created_routines')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Not a join table btw Routine and Students because the Attitude model depends on this model. i.e it has a field ->
# attitudes
class StudentRoutine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    routine = models.ForeignKey("Routine", on_delete = models.CASCADE, related_name="student_routines")
    student = models.ForeignKey("Student", on_delete=models.CASCADE, related_name="routines")
    message = models.TextField("message/request")
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('AdminPerson', on_delete=models.DO_NOTHING, related_name='created_student_routines')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} routine for {}".format(self.student.full_name, self.routine.date)
