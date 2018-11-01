from django.contrib import admin
from crumbs.models import Activity, ActivityItem

class ActivityItemInline(admin.StackedInline):
    model = ActivityItem

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [ActivityItemInline]

