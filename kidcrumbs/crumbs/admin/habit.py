from django.contrib import admin
from crumbs.models import Habit, HabitOption

class HabitOptionInline(admin.StackedInline):
    model = HabitOption

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    save_as = True
    inlines = [HabitOptionInline]

