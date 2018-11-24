from django.contrib import admin
from crumbs.models import Announcement


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    save_as = True
    raw_id_fields = ['announcer']
