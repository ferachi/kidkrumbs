from django.db import models
import uuid


class Membership(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='memberships')
    group = models.ForeignKey('Group', verbose_name="group", on_delete=models.CASCADE, related_name='memberships')
    reason = models.CharField(max_length=200, blank=True)
    is_current = models.BooleanField(default=True)
    date_joined = models.DateField()
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} membership for {1}".format(self.group.slug, self.person.full_name)

    class Meta:
        unique_together = ('person','group')
        ordering = ('-date_joined',)
