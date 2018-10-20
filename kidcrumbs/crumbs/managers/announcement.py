from django.db import models


class AnnouncementManager(models.Manager):
    def public(self):
        return self.get_queryset().filter(is_private=False)
