from django.db import models
from django.utils.text import slugify
from datetime import datetime, date
from django.urls import reverse
import uuid

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40,help_text="e.g Session 20xx/20yy")
    slug = models.SlugField(max_length=50, blank=True, null=True, unique=True)
    description = models.TextField(help_text="what to expect in this session")
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField("is this the current session?", default=False,
                                     help_text="setting this option makes this session current while disabling any other.")
    school = models.ForeignKey('School', related_name='sessions', on_delete=models.CASCADE)
    created_by = models.ForeignKey("AdminPerson", on_delete=models.DO_NOTHING, null=True, related_name="created_sessions")
    created_date = models.DateField(auto_now_add=True)
    timestamp = models.DateField(auto_now=True)

    @property
    def session_year(self):
        return "{} / {}".format(self.start_date.year, self.end_date.year)

    @property
    def session_duration(self):
        return "{} - {}".format(self.start_date.year, self.end_date.year)

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        slug = "{0}-{1}".format(self.school.slug,self.session_year)
        self.slug = slugify(slug)
        super(Session, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-start_date']
