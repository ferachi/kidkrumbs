from django.contrib import admin
from django import forms
from crumbs.models import SchoolGroup, Membership, Classroom, Student, Enrollment, Person
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from crumbs.forms.membership import MembershipAdminForm


class GroupListFilter(admin.SimpleListFilter):
	# Human-readable title which will be displayed in the
	# right admin sidebar just above the filter options.
	title = _('Categories')

	# Parameter for the filter that will be used in the URL query.
	parameter_name = 'group'

	def lookups(self, request, model_admin):
		"""
		Returns a list of tuples. The first element in each
		tuple is the coded value for the option that will
		appear in the URL query. The second element is the
		human-readable name for the option that will appear
		in the right sidebar.
		"""
		return (
			('classroom', _('Classrooms')),
			('group', _('Groups')),
			('department', _('Departments')),
		)

	def queryset(self, request, queryset):
		"""
		Returns the filtered queryset based on the value
		provided in the query string and retrievable via
		`self.value()`.
		"""

		if self.value() == 'classroom':
			return queryset.filter(group__category='CL')
		if self.value() == 'group':
			return queryset.exclude(Q(group__category='CL') | Q(group__category='DP'))
		if self.value() == 'department':
			return queryset.filter(group__category='DP')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	form = MembershipAdminForm
	raw_id_fields = ['person', 'group']
	list_display = ['group_person', 'group_name','group_session']
	list_filter = [GroupListFilter, 'group__session']
	# search_fields = ['^group__name']
	ordering = ['person']

	def group_person(self, obj):
		return "{} {} {}".format(obj.person.user.first_name, obj.person.user.other_names, obj.person.user.last_name)
	group_person.admin_order_field = 'person__user__first_name'
	group_person.short_description = 'member'

	def group_name(self, obj):
		return obj.group.group_name
	group_name.admin_order_field = 'group__group_name'
	group_name.short_description = 'name'

	def group_session(self, obj):
		return obj.group.session
	group_session.admin_order_field = 'group__session__name'
	group_session.short_description = 'session'


	def save_model(self, request, obj, form, change):
		if obj.group.category == 'CL':
			# make sure the only person to have this membership to classroom is a student
			try:
				classroom = obj.group.classroom  # checking if the membership is for classrooms
				# change all current memberships to false
				if obj.is_current:
					current_classrooms_memberships = Membership.objects.filter(group__category='CL', person=obj.person, is_current=True)
					for membership in current_classrooms_memberships:
						membership.is_current = False
						membership.save()

				# modify the student enrollment if person is a student
				try:
					student = Student.objects.get(pk=obj.person.pk)
					courses = classroom.courses.all()
					# for each course in the classrooms courses modify the students enrollment
					for course in courses:
						try:
							enrollment = Enrollment.objects.get(student=student, course=course)
						except Enrollment.DoesNotExist:
							enrollment = Enrollment()
							enrollment.student = student
							enrollment.course = course
							enrollment.session = obj.group.session
							enrollment.save()
				except Student.DoesNotExist:
					pass
			except Classroom.DoesNotExist:
				pass

		else:
			if obj.is_current == True:
				current_group_memberships = Membership.objects.filter(group__name=obj.group.name, group__category=obj.group.category, person=obj.person, is_current=True)
				for membership in current_group_memberships:
					membership.is_current = False
					membership.save()
		obj.save()
