from django.contrib import admin
from crumbs.models import AssessmentType, Assessment, AssessmentResult, Grade, Subject, GradeSystem, AssessmentPaper
from django import forms

@admin.register(AssessmentType)
class AssessmentType(admin.ModelAdmin):
    save_as = True

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'assessment_type', 'max_score', 'term']
    list_filter = ['term__session', 'assessment_type','subject__core_subject']
    search_fields = ['^subject__subject_code', '^assessment_type__name']
    ordering = ['subject__subject_code', 'max_score']
    raw_id_fields = ['subject']
    save_as = True


class AssessmentResultAdminForm(forms.ModelForm):
    class Meta:
        model = AssessmentResult
        fields = '__all__'

    def clean(self):
        cleaned_data =  self.cleaned_data
        enrollment = cleaned_data.get("enrollment")
        assessment = cleaned_data.get("assessment")
        term = assessment.term
        date_taken = cleaned_data.get("date_taken")
        score = cleaned_data.get("score")

        if enrollment.subject != assessment.subject:
            raise forms.ValidationError(
                    'assessment selected does not pertain to the enrollment'
            )
        if term.start_date < enrollment.subject.session.start_date or term.end_date > enrollment.subject.session.end_date:
            self.add_error('assessment','The session the assessment was taken differs from the session when the student was enrolled.')
            raise forms.ValidationError(
                        'Selected Assessment Session does not conform to the selected Enrollment Session.'
                )
        if date_taken < term.start_date or date_taken > term.end_date:
            self.add_error('date_taken', "date selected falls outside the term selected")

        if score > assessment.max_score:
            self.add_error('score', "score can't be greater than maximum attainable score of %s in assessment" % assessment.max_score)

        existing_result = AssessmentResult.objects.filter(enrollment=enrollment, assessment=assessment)
        if existing_result.exists():
            raise forms.ValidationError(
                'A result already exist for this enrollment in this term'
            )

@admin.register(AssessmentResult)
class AssessmentResultAdmin(admin.ModelAdmin):
    raw_id_fields = ['enrollment', 'assessment']
    form = AssessmentResultAdminForm
    list_display = ['student', 'assessment_type','score', 'subject_name', 'term']
    list_filter = ['assessment__term__session','assessment__assessment_type','assessment__subject']
    search_fields = ['^enrollment__student__first_name','^enrollment__student__last_name','^assessment__assessment_type__name','^assessment__subject__subject_code']
    save_as = True

    def subject_name(self,obj):
        return obj.assessment.subject
    subject_name.short_description = 'Subject'
    subject_name.admin_order_field = 'assessment__subject__subject_code'

    def assessment_type(self, obj):
        return obj.assessment.assessment_type

    assessment_type.short_description = 'Assessment'
    assessment_type.admin_order_field = 'assessment__assessment_type__name'

    def student(self, obj):
        return obj.enrollment.student

    student.short_description = 'Student'
    student.admin_order_field = 'enrollment__student__first_name'

    def term(self, obj):
        return obj.assessment.term

    term.short_description = 'Term'
    term.admin_order_field = 'assessment__term__name'


admin.site.register(Grade)
admin.site.register(GradeSystem)

class AssessmentPaperForm(forms.ModelForm):
    class Meta:
        fields = '__all__'

    def clean(self):
        cleaned_data = super(AssessmentPaperForm, self).clean()
        classroom = cleaned_data.get('classroom')
        assessment = cleaned_data.get('assessment')
        print(classroom, assessment)
        if assessment.term.session != classroom.session:
            raise forms.ValidationError('The session this Assessment was conducted does not conform to this Classrooms session')
        if assessment.subject not in classroom.subjects.all():
            raise forms.ValidationError('This Classroom does not offer the Subject that this Assessment was conducted for.')

@admin.register(AssessmentPaper)
class AssessmentPaperAdmin(admin.ModelAdmin):
    list_display = ['name','classroom','session']
    raw_id_fields = ['assessment', 'classroom']
    form = AssessmentPaperForm
    search_fields = ['^name','classroom__name']
    list_filter = ['assessment__term__session','assessment__subject']

    def session(self, obj):
        return obj.classroom.session.session_duration

    # session.short_description = 'session'
    # session.admin_order_field = 'session__start_date'
