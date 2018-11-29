from django import forms
from crumbs.models import Membership, Student, Person

class MembershipAdminForm(forms.ModelForm):
	class Meta:
		model = Membership
		fields = '__all__'

	def clean(self):
		date_joined = self.cleaned_data.get('date_joined')
		term = self.cleaned_data.get('term')
		group = self.cleaned_data.get('group')
		
		person = self.cleaned_data.get('person')
		if not term:
			raise forms.ValidationError("Please select a term")
		if not person:
			raise forms.ValidationError("Please select a  Member")
		if not date_joined:
			raise forms.ValidationError("Please enter the date this Member joined this Group")
			
		start_date = term.start_date
		end_date = term.end_date
		if (start_date > date_joined) or (end_date < date_joined):
			self.add_error('date_joined', "date joined falls outside the term selected")

		if(term.session != group.session):
			raise forms.ValidationError("Group's session falls outside the selected terms session")

		user_groups = list(person.user.groups.values_list('name',flat=True))
		if 'students' not in user_groups and group.category == 'CL':
			self.add_error('person','Only Students can be members of a classroom')

		if 'school administrators' not in user_groups and group.category == 'DP':
			self.add_error('person','Only Staffs can be members of a Department')



		# if this membership is new
		if not self.instance.pk:
			try:
				student = Student.objects.get(pk=person.pk)
				class_membership = student.memberships.filter(group__category='CL', term__session=term.session)
				if group.category == 'CL' and class_membership.exists():
					raise forms.ValidationError(
						"Student already belongs to a classroom within this session"
					)
				
			except Student.DoesNotExist:
				pass
			try:
				_person = Person(pk=person.pk)
				group_membership = _person.memberships.filter(group=group, term__session=term.session)
				if group_membership.exists():
					raise forms.ValidationError(
						"Person already has membership to this group within this session"
					)
			except Person.DoesNotExist:
				pass
