from django.conf.urls import url, include
from .views import AppView
from crumbsauth.views import TokenView 
from crumbs.viewsets import *

from rest_framework.routers import DefaultRouter

app_name = 'crumbsapp'

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'activity-items', ActivityItemViewSet)
router.register(r'activity-comments', ActivityCommentViewSet)
router.register(r'activity-comment-replies', ActivityCommentReplyViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'habits', HabitViewSet)
router.register(r'habit-options', HabitOptionViewSet)
router.register(r'habit-responses', HabitResponseViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'people', PersonViewSet)
router.register(r'routines', RoutineViewSet)
router.register(r'schools', SchoolViewSet)
router.register(r'students', StudentViewSet)
router.register(r'student-routines', StudentRoutineViewSet)

urlpatterns = [
    url(r'^$', AppView.as_view(), name='home'),
    url(r'^token/$', TokenView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^.*/$',AppView.as_view(),name='any_other')
]
