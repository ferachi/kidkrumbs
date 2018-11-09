from rest_framework import permissions
from crumbs.models import Student, Person, PersonSchoolRole

class CanViewStudents(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):

        # Only permit read only 
        if request.method in permissions.SAFE_METHODS:
            
            # for fercube staffs
            if request.user.is_admin and request.user.is_active:
                return True

            # for the student
            if request.user == obj.user:
                return True

            # if parent request

            # check for the relationship with the current user
            relation = obj.source_relations.filter(relative__user = request.user)

            if relation.exists() and relation[0].relationship_type in ['PT','GN']:
                return True

            # check for the admin
            
            # get the schools of the student
            student = Person.objects.get(user = obj.user)
            person = Person.objects.get(user=request.user)

            student_school_roles = PersonSchoolRole.objects.filter(person=student, roles__name="student")
            
            schools = list(map(lambda x : x.school.id, student_school_roles))
            user_roles = person.person_school_roles.filter(school__in=schools)
            
            if not user_roles.exists():
                return False
            
            for user_role in user_roles:
                roles = {role.name for role in user_role.roles.all()}
                if len(roles & {"administrative"}) > 0:
                    return True

            return False

        return False

