from django.db import models
from django.utils.text import slugify
import uuid

class Term(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TERMS = (
        ('FT', 'First Term'),
        ('ST', 'Second Term'),
        ('TT', 'Third Term'),
        ('AT', 'Auxiliary Term')
    )
    session = models.ForeignKey('Session', on_delete=models.CASCADE, related_name='terms')
    name = models.CharField("Term", max_length=2, choices=TERMS)
    slug = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {}".format(self.name, self.session.session_duration)

    def save(self, *args, **kwargs):
        self.slug = slugify("%s-%s-%s" % (self.session.school.short_name,self.name,self.session.session_year))
        super(Term, self).save(*args, **kwargs)
