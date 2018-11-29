from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import StudentSerializer, GroupSerializer, MembershipSerializer, StudentGroupSerializer,\
StudentRoutineSerializer, SubjectSerializer,EnrollmentSerializer, ClassroomSerializer, StudentResultSerializer
from crumbs.models import Student, Group, Membership, StudentRoutine, Subject, Enrollment, Classroom, AssessmentResult
from crumbs.permissions import CanViewStudents


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (CanViewStudents,)
    lookup_field = 'username'

    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_admin and user.is_active:
    #         return Student.objects.all
    #
    #     # check for the relationship with the current user
    #     students = Student.objects.filter(source_relations__relative__user = request.user,\
    #                 source_relations__relationship_type__in=['PT','GN'])
    #


    @detail_route()
    def get_groups(self, request, username=None):
        """
        Gets the Students' groups
        """
        student = self.get_object()
        groups = Group.objects.filter(memberships__person=student)
        serializer = StudentGroupSerializer(groups, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_classrooms(self, request, username=None):
        """
        Gets the Students' classrooms
        """
        student = self.get_object()
        groups = Classroom.objects.filter(memberships__person=student)
        serializer = ClassroomSerializer(groups, many=True)
        return Response(serializer.data)


    @detail_route()
    def get_current_groups(self, request, username=None):
        """
        Gets the Students' groups
        """
        student = self.get_object()
        groups = Group.objects.filter(memberships__person=student, memberships__is_current = True)
        serializer = StudentGroupSerializer(groups, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_memberships(self, request, username=None):
        """
        Gets the Students' memberships to groups
        """
        student = self.get_object()
        memberships = Membership.objects.filter(person=student)
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_routines(self, request, username=None):
        """
        Gets the Students' routines(habits)
        """
        student = self.get_object()
        routines = StudentRoutine.objects.filter(student=student)
        serializer = StudentRoutineSerializer(routines, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_routines_by_group(self, request, username=None):
        """
        Gets the Students' routines(habits) by a group specified
        """
        group = request.query_params.get('group')
        student = self.get_object()
        if group:
            routines = StudentRoutine.objects.filter(routine__group__id__exact=group,student=student)
            serializer = StudentRoutineSerializer(routines, many=True)
            return Response(serializer.data)
        return ([])

    @detail_route()
    def get_subjects(self, request, username=None):
        """
        Gets the Students' subjects
        """
        student = self.get_object()
        subjects = Subject.objects.filter(enrollments__student=student)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_results(self, request, username=None):
        """
        Gets the Students' results
        """
        student = self.get_object()
        results = AssessmentResult.objects.filter(enrollment__student=student)
        serializer = StudentResultSerializer(results, many=True)
        return Response(serializer.data)

    @detail_route()
    def get_enrollments(self, request, username=None):
        """
        Gets the Students' enrollments
        """
        student = self.get_object()
        enrollments = Enrollment.objects.filter(student=student)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)
