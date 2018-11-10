from django.db import models
import uuid


class Habit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True)
    school = models.ForeignKey('School', related_name='habits', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('AdminPerson', on_delete=models.DO_NOTHING, related_name='created_habits')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HabitOption(models.Model):
    TYPES = (
        ("CH", "choice"),
        ("TX", "text"),
        ("DT", "date")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    habit = models.ForeignKey(Habit, on_delete = models.CASCADE, related_name="options")
    title = models.CharField(max_length=20, blank=True)
    habit_type = models.CharField("type", max_length=2, choices=TYPES, default="CH")
    index = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('AdminPerson', on_delete=models.DO_NOTHING, related_name='created_habit_options')
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['index','title']


class HabitResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    habit_option = models.ForeignKey("HabitOption", on_delete=models.CASCADE, related_name="responses", null=True, blank=True)
    student_routine = models.ForeignKey("StudentRoutine", on_delete =models.CASCADE, related_name="habits")
    # should default to title in habit option; only type in
    # a title if there is no option.
    title = models.CharField(max_length=20, blank=True)
    value = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.habit_option:
            self.habit_option.title
        return self.title
