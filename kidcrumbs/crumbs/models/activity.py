from django.db import models
import uuid
from crumbs.utils import COLORS


class Activity(models.Model):
    """
        Activity
        This model contains fields that defines a groups' activity
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='activities')
    note = models.TextField("teachers comment", default="new activity")
    color = models.CharField(max_length=20, choices=COLORS, default='DODGERBLUE')
    tags = models.CharField(max_length=150, help_text="tags seperated by commas", blank=True)
    date = models.DateField()
    created_by = models.ForeignKey('AdminPerson', on_delete=models.DO_NOTHING, related_name='activities')
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    @property
    def name(self):
        return self.__str__()

    def __str__(self):
        return "{0} activity for {1}".format(self.group,self.date)

    class Meta:
        verbose_name_plural = 'activities'
        ordering = ['-date']


class ActivityItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    time = models.TimeField(null=True, blank=True)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, related_name='activities')
    color = models.CharField(max_length=20, choices=COLORS, default='DODGERBLUE')
    created_by = models.ForeignKey('AdminPerson', on_delete=models.DO_NOTHING, related_name='created_activities')
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "".format(self.title)

    class Meta:
        verbose_name_plural = 'activity items'
        ordering = ['-created_date', 'title']


class ActivityComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='activity_comments')
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE, related_name='activity_comments')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}'s comment on {1}".format(self.person.full_name, self.activity.name)

    class Meta:
        ordering = ['-created_date']


class ActivityCommentReply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='comment_replies')
    activity_comment = models.ForeignKey('ActivityComment', on_delete=models.CASCADE, related_name='replies')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}'s reply to {1}".format(self.person.full_name, self.activity_comment.person.full_name)

    class Meta:
        ordering = ['-created_date']

