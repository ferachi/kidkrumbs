from rest_framework import permissions, viewsets, status
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from crumbs.serializers import StudentSerializer, GroupSerializer, MembershipSerializer, StudentGroupSerializer,\
StudentRoutineSerializer, SubjectSerializer,EnrollmentSerializer, ClassroomSerializer, StudentResultSerializer
from crumbs.models import Student, Group, Membership, StudentRoutine, Subject, Enrollment, Classroom, AssessmentResult
from crumbs.permissions import CanViewStudents
from itertools import groupby


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
        print(len(routines), 'length of routines')
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
    def get_term_result_positions(self, request, username=None):
        """
            Gets the position (using scores obtained in a term) of the student when
            compared with peers using his/her total scores
        """
        student = self.get_object()

        # the students' classrooms
        student_classrooms = []

        # term results
        results = []

        # for each group the student belongs to get
        # the classroom;
        for group in student.group_list.all():
            try:
                student_classrooms.append(group.classroom)
            except:
                pass

         # for each classroom get all results
         # get all the students, each student has results
        for classroom in student_classrooms:

            # making sure the membership in classroom are only students
            classroom_students = classroom.members.filter(person_school_roles__roles__name='student')

            #used to combine all the students results
            student_results = []

            for _student in classroom_students:
                # get each students resuls
                _results = AssessmentResult.objects.filter(enrollment__student__user__id=_student.user.id,\
                         assessment__term__session=classroom.session)\
                         .values('enrollment__student__user__id','score','assessment__max_score',\
                         'assessment__subject', 'assessment__term__id', 'assessment__term__end_date')

                student_results += list(_results)

            # holds a list of terms' results (which is a list of students results) 
            classroom_term_results = []

            # prerequisite for sorting
            student_results_sorted = sorted(list(student_results).copy(), key=lambda res : res['assessment__term__id'])

            # group by term 
            for k,g in groupby(student_results_sorted, lambda res : res['assessment__term__id']):
                # convert the values to a list
                _groups = list(g)

                # sort by student
                sorted_results = sorted(_groups, key=lambda res: res['enrollment__student__user__id'])
                term_results = []

                # groupby student
                for i,s in groupby(sorted_results, lambda res : res['enrollment__student__user__id']):
                    #students' result
                    _results = list(s)

                    # students total score for the term
                    student_total_scores = sum(map(lambda res : res['score'], _results))

                    # the maximum scores
                    maximum_scores = sum(map(lambda res : res['assessment__max_score'],_results))

                    term_results.append({'id':i, 'term_id':k, 'total_scores':student_total_scores,\
                        'max_scores':maximum_scores})

                classroom_term_results.append(term_results) # this holds a list of term results

            for _term_results in classroom_term_results:
                # number of results
                no_results = len(_term_results)

                # map the total_scores into classroom score set
                # using a set so if 2 students have same score they are awarded same position
                classroom_scores = sorted(list(set(map(lambda res : res['total_scores'],\
                                   _term_results))), reverse=True) # in desc order

                # get the student result from the _term_results
                student_result = list(filter(lambda res : res['id'] == student.user.id, _term_results))[0]

                #get the position
                student_result['position'] = classroom_scores.index(student_result['total_scores']) + 1
                student_result['total_count'] = no_results

                # get index of the student in the sorted results
                results.append(student_result)
        
        return Response(results)


    @detail_route()
    def get_enrollments(self, request, username=None):
        """
        Gets the Students' enrollments
        """
        student = self.get_object()
        enrollments = Enrollment.objects.filter(student=student)
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)
