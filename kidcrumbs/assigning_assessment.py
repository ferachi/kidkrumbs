# IPython log file

from crumbs.models import Session
session = Session.objects.filter(start_data__contains='2017')
session = Session.objects.filter(start_date__contains='2017')
session
session = session[0]
session
from crumbs.models import Assessment
assessments = Assessment.objects.all()
from crumbs.models import Term
terms = Term.objects.filter(session__start_date__contains="2017")
terms
t=terms[0]
t.name
for term in terms:
    for assessment in assessments:
        if assessment.term.name == term.name:
            assessment.pk = None
            assessment.id = None
            assessment.term = term
            assessment.save()
            
get_ipython().run_line_magic('help', '')
help
help()
get_ipython().run_line_magic('magic', '')
get_ipython().run_line_magic('log', '')
help()
from crumbs.models import Person
jane = Person.objects.get(user.username="jane_ephraim")
jane = Person.objects.get(user.username="jane_ephraim")
jane = Person.objects.get(user__username="jane_ephraim")

get_ipython().run_line_magic('logstart', '')
get_ipython().run_line_magic('logstop', '')
get_ipython().run_line_magic('logstart', 'assigning_assessment.py')
enrollments = jane.enrollments.all()
get_ipython().run_line_magic('logoff', '')
get_ipython().run_line_magic('logoff', '')
for enrollment in enrollments:
    for assessment in enrollment.subject.assessments.all():
        score = random.randint(assessment.max_score/2, assessment.max_score)
        AssessmentResult.objects.create(assessment=assessment, enrollment=enrollment, date_taken=assessment.term.end_date, score=score)
        
       
