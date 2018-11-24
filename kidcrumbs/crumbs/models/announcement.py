from django.db import models
from django.urls import reverse
import uuid
from django.conf import settings
from crumbs.managers import AnnouncementManager

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=120)
    overview = models.CharField("brief description",max_length=200, blank=True)
    content = models.TextField("announcement")
    announcer = models.ForeignKey("Person", on_delete=models.DO_NOTHING)
    term = models.ForeignKey('Term', on_delete=models.CASCADE, related_name='announcements')
    is_private = models.BooleanField(default=False, help_text='setting this would make this announcement visible to only registered users.')
    published_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    objects = AnnouncementManager()

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ['-published_date']

class AnnouncementQuestion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='announcement_questions')
    announcement = models.ForeignKey('Announcement', on_delete=models.CASCADE, related_name='announcement_questions')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}'s question on {1}".format(self.person.full_name, self.announcement.name)

    class Meta:
        ordering = ['-created_date']


class AnnouncementQuestionReply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='announcement_question_replies')
    announcement_question = models.ForeignKey('AnnouncementQuestion', on_delete=models.CASCADE, related_name='replies')
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}'s reply to {1}".format(self.person.full_name, self.announcement_question.person.full_name)

    class Meta:
        ordering = ['-created_date']

