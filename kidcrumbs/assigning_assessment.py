enrollments = Enrollment.objects.all()
for enrollment in enrollments:
    for assessment in enrollment.subject.assessments.all():
        score = random.randint(round(assessment.max_score/5), assessment.max_score)
        AssessmentResult.objects.create(assessment=assessment, enrollment=enrollment, date_taken=assessment.term.end_date, score=score)
        
       
