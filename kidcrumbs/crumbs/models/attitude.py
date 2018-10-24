from django.db import models
import uuid


class Attitude(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student_routine = models.ForeignKey("StudentRoutine", on_delete =models.CASCADE, related_name="attitudes")
    habit = models.ForeignKey("Habit", on_delete = models.DO_NOTHING, related_name="attitudes", null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}: {} for {}".format(self.student_routine.student,self.habit, self.student_routine.routine.date)


class AttitudeResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    habit_option = models.ForeignKey("HabitOption", on_delete=models.CASCADE, related_name="responses", null=True, blank=True)
    attitude = models.ForeignKey("Attitude", on_delete=models.CASCADE, related_name="responses")
    # should default to title in habit option; only type in
    # a title if there is no option.
    title = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.habit_option:
            self.habit_option.title
        return self.title
