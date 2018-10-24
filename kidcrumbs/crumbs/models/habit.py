from django.db import models
import uuid


class Habit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True)
    school = models.ForeignKey('School', related_name='habits', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
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
    title = models.CharField(max_length=20)
    habit_type = models.CharField("type", max_length=2, choices=TYPES, default="CH")
    index = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['index','title']


