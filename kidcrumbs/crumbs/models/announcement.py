from django.db import models
from django.urls import reverse
import uuid
from django.conf import settings
from crumbs.managers import AnnouncementManager

class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    term = models.ForeignKey('Term', on_delete=models.CASCADE, related_name='announcements')
    title = models.CharField(max_length=120)
    overview = models.CharField("brief description",max_length=200, blank=True)
    content = models.TextField("announcement")
    announcer = models.ForeignKey("Person", on_delete=models.DO_NOTHING)
    is_private = models.BooleanField(default=False, help_text='setting this would make this announcement visible to only registered users.')
    published_date = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    objects = AnnouncementManager()

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        ordering = ['-published_date']
