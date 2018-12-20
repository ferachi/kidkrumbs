from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import SchoolSerializer, GroupSerializer, SubjectSerializer, GradeSystemSerializer,\
        StudentSerializer, ClassroomSerializer,SessionSerializer
from crumbs.models import School, Group, Subject, GradeSystem, Session, Student, Classroom,Session



class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

    @detail_route()
    def get_sessions(self, request, pk=None):
        """
        Gets the Schools' Sessions
        """
        school = self.get_object()
        sessions = Session.objects.filter(school=school)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_groups(self, request, pk=None):
        """
        Gets the Schools' groups
        """
        school = self.get_object()
        groups = Group.objects.filter(session__school=school)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_classrooms(self, request, pk=None):
        """
        Gets the Schools' Classrooms
        """
        school = self.get_object()
        classrooms = Classroom.objects.filter(session__school=school)
        serializer = ClassroomSerializer(classrooms, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_subjects(self, request, pk=None):
        """
        Gets the Schools' subjects
        """
        school = self.get_object()
        subjects = Subject.objects.filter(session__school=school)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_grade_system(self, request, pk=None):
        """
        Gets the Schools' grading system
        """
        school = self.get_object()
        gradesystem = GradeSystem.objects.get(school=school, is_current=True)
        serializer = GradeSystemSerializer(gradesystem)
        return Response(serializer.data)

    @detail_route()
    def get_current_students(self, request, pk=None):
        """
        Gets the Schools' current students
        """
        school = self.get_object()
        current_session = Session.objects.get(school=school, is_current=True)
        students = Student.objects.filter(group_list__session=current_session)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
