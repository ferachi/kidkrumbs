from django.contrib import admin
from crumbs.models import Membership


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    save_as = True

