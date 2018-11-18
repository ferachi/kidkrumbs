from django.db import models
from .group import Group, AbstractGroup
import uuid


class SchoolGroupBase(AbstractGroup):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class SchoolGroup(Group):
	group_base = models.ForeignKey(SchoolGroupBase, related_name="school_groups", on_delete=models.CASCADE)

	@property
	def name(self):
		return "{}".format(self.group_base.name)

	@property
	def full_name(self):
		return "{}-{} {}".format(self.group_base.school.short_name, self.group_base.name, self.session.session_year)
