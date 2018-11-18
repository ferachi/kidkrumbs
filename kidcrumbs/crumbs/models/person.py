from django.db import models
from .user import User
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse
from crumbs.managers import AdminPersonManager, NonAdminPersonManager, RelativeManager, \
TeacherManager, HeadTeacherManager, StudentManager, SchoolPersonManager, ExternalPersonManager, \
SuperAdminPersonManager, OtherAdminPersonManager
from crumbs.utils.image_uploaders import upload_person_avatars_dir
from django.core.validators import RegexValidator


import uuid


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='person')
    avatar = models.ImageField('image',null=True, blank=True,upload_to=upload_person_avatars_dir, help_text='Use square dimensional images, or images will be cropped automatically.')
    GENDER = (
        ('M', 'male'),
        ('F', 'female'),
    )
    title = models.CharField(max_length=20, blank=True)
    description = models.TextField("Brief Description", blank=True)
    occupation = models.CharField(max_length=120, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, default='F')
    dob = models.DateField("date of birth", null=True, blank=True)
    hobbies = models.CharField(max_length=300, blank=True, help_text="Specify hobbies separated by commas")
    qualifications = models.CharField(max_length=150, help_text='qualifications separated with commas', blank=True)
    email_confirmed = models.BooleanField(default=False)
    relatives = models.ManyToManyField('self', through='Relation', through_fields=('person','relative'), symmetrical=False, blank=True)
    username = models.CharField(max_length=150, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if len(self.full_name) > 3:
            return self.full_name
        return self.user.email

    @property
    def full_name(self):
        if self.user.other_names:
            return "{} {} {}".format(self.user.last_name, self.user.other_names, self.user.first_name)
        return "{} {}".format(self.user.last_name, self.user.first_name)

    def save(self, *args, **kwargs):
        self.username = self.user.username
        super(Person, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "People"



class PersonContact(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?(234)?\d{9,11}$', message="Phone number to be entered in the format: '+234-XX...' or '0X0-XX'. Up to 13 digits allowed.")
    person = models.OneToOneField('Person', primary_key=True, related_name='contact', on_delete=models.CASCADE)
    address_one = models.TextField("first address")
    address_two = models.TextField("second address", blank=True)
    mobile_number = models.CharField(max_length=13, validators=[phone_regex])
    mobile_number_two = models.CharField(max_length=13, blank=True, validators=[phone_regex])
    home_number = models.CharField(max_length=13, blank=True, validators=[phone_regex])
    office_number = models.CharField(max_length=13, blank=True, validators=[phone_regex])
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "contact for {}".format(self.person.full_name)


class Role(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class PersonSchoolRole(models.Model):
    """
    The Persons School Role
    This assigns a particular role for each user in the school
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    person = models.ForeignKey(Person, related_name="person_school_roles", on_delete=models.CASCADE)
    roles = models.ManyToManyField("Role", related_name="person_school_roles")
    school = models.ForeignKey("School", related_name="person_roles", on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Roles for %s in %s" % ( self.person.full_name, self.school.name)

    class Meta:
        verbose_name_plural = "Peoples' School Roles"
        unique_together = ('person','school')


class Relation(models.Model):
    """
        The Relations Model
        Defines the relationship between a target (relative field) and person (source field)
        As an example
        - If a Mother is defined as the source and a student defined as the target
        then the relationship between student and the Mother is defined in the relationship field as "Son/Daughter"
        and the relationship_type field as "Child"
        - If a Student is defined as the source and a father defined as the target 
        then the relationship between father and student is defined in the relationship field as "Father"
        and the relationship_type as "Parent"

    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # the person who has the relation (source)
    # e.g a student.source_relations.all()[0].relative to get the students relative person e.g mother
    # same as student.relatives.all()[0]
    # student.source_relations.all() gets a querset of relations
    # the field on the Person Object 'relatives' i.e student.relatives.all() gets a queryset of people
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='source_relations')

    # The relative to the person (target)
    # e.g a father.target_relations.all()[0].person to get the fathers relative e.g child, wife etc
    # same as father.person_set.all()[0] ; because symmetrical is false
    relative = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='target_relations')

    RELATIONSHIP_TYPE = (
        ('PT', 'parent'),
        ('GN', 'guardian'),
        ('CD', 'child'),
        ('SB', 'sibling'),
        ('CN', 'cousin'),
        ('OT', 'other')
    )
    relationship = models.CharField(max_length=20, help_text="E.g Father, Mother, Sister, Uncle")
    relationship_type = models.CharField(max_length=2, choices=RELATIONSHIP_TYPE)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s relationship with %s" % (self.person, self.relative)


class Student(Person):
    class Meta:
        proxy = True
    objects = StudentManager()


class Teacher(Person):
    class Meta:
        proxy = True
    objects = TeacherManager()

# A user who belongs to a school
class SchoolPerson(Person):
    class Meta:
        proxy = True
        verbose_name_plural = 'School People'
    objects = SchoolPersonManager()


# Administrative people - Teachers, SuperAdmin and OtherAdmin
class AdminPerson(Person):
    class Meta:
        proxy = True
        verbose_name_plural = 'Administrative People'
    objects = AdminPersonManager()


class SuperAdminPerson(Person):
    class Meta:
        proxy = True
        verbose_name_plural = 'Super Administrative People'
    objects = SuperAdminPersonManager()


class OtherAdminPerson(Person):
    class Meta:
        proxy = True
        verbose_name_plural = 'Other Administrative People'
    objects = OtherAdminPersonManager()


# Non Administrative Staff
class NonAdminPerson(Person):
    class Meta:
        proxy = True
        verbose_name_plural = 'Non Administrative People'
    objects = NonAdminPersonManager()


# Parents/Guardians and Others related to students 
class ExternalPerson(Person):
    class Meta:
        proxy = True
        verbose_name_plural = 'External People'
    objects = ExternalPersonManager()

