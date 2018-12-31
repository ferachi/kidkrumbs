from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.urls import reverse
from crumbs.utils.image_uploaders import *
from crumbs.utils.validators import validate_location
from django.core.validators import RegexValidator
import uuid
from crumbs.utils.colors import COLORS
from .user import User


class School(models.Model):
    GENDER = (
        ('MA', 'Male'),
        ('FE', 'Female'),
        ('MI', 'Mixed')
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    short_name = models.CharField(max_length=10, unique=True, help_text="Abbreviated Name; A text composed of the first letters in school's name.")
    brief_description = models.CharField("caption",max_length=500)
    description = models.TextField(help_text="simple description of your school")
    motto = models.CharField(max_length=200)
    vision = models.CharField(max_length=300)
    gender = models.CharField(max_length=2, choices=GENDER, default='MI')
    proprietor = models.CharField(max_length=200)
    year_established = models.DateField(help_text="month/day/year")
    color = models.CharField(max_length=20, default="TEAL", choices=COLORS)
    logo = models.ImageField("school logo", null=True,upload_to=upload_school_logo_dir)
    thumb_image = models.ImageField("thumbnail image",null=True,blank=True, upload_to=upload_school_images_dir, help_text="The image you would like to display to your visitors alongside other schools")
    home_image = models.ImageField(null=True, blank=True, upload_to=upload_school_images_dir, help_text="image you'd like your visitors to see on your home page")
    about_image = models.ImageField(null=True, blank=True, upload_to=upload_school_images_dir, help_text="image you'd like to be displayed on your about page")
    is_public = models.BooleanField(default=False, help_text='is this a  public school?')
    tuition_range = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name='created_schools', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.short_name = slugify(self.short_name)
        self.slug = slugify("%s" % (self.name))
        super(School, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('knob:school:index'))

    class Meta:
        verbose_name_plural = 'School'


class SchoolContact(models.Model):
    # nigerian phone numbers
    phone_regex = RegexValidator(regex=r'^\+?(234)?\d{9,11}$', message="Phone number to be entered in the format: '+234-XX...' or '0X0-XX'. Up to 13 digits allowed.")

    school = models.OneToOneField(School, primary_key=True, on_delete=models.CASCADE, related_name='contact')
    address = models.TextField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30, default='Nigeria')
    email = models.EmailField()
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    phone_number2 = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    phone_number3 = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    facebook_link = models.URLField(blank=True)
    googleplus_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    website = models.URLField(blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.school.name


class SchoolFacility(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='facilities')
    name = models.CharField(max_length=150)
    quantity = models.PositiveSmallIntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class SchoolService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=400)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SchoolRequirement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='requirements')
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    hierarchy = models.PositiveSmallIntegerField("order",default=1) # the order in which it should be listed
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('hierarchy',)

class SchoolRequirementItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    requirement = models.ForeignKey('SchoolRequirement', on_delete=models.CASCADE, related_name='requirement_items')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    hierarchy = models.PositiveSmallIntegerField(default=1) # the order in which it should be listed
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('hierarchy',)
        unique_together = ('requirement','hierarchy')


class SchoolGallery(models.Model):
    """
    The School Gallery Model
    On the main application, this will serve as an Album
    The album will contain a
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey('School', on_delete=models.CASCADE, related_name='galleries')
    name = models.CharField(max_length=50) # name of the album
    description = models.TextField(null=True, blank=True) # a brief description
    max_num_images = models.PositiveSmallIntegerField(default=20, editable=False) # maximum number of images per gallery
    is_public = models.BooleanField(default=True) # can this gallery be shown to the public (external people)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" %( self.name, "album")


class SchoolImage(models.Model):
    """
    The School Image
    The different images to be uploaded by the school people (Admin, Teachers and Students)
    This will be displayed in it's respective Gallery
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gallery = models.ForeignKey('SchoolGallery', on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=50) # title to be captioned when displayed
    description = models.TextField(null=True, blank=True) # basic description of image. To display during slide show if any
    image = models.ImageField(upload_to=upload_school_gallery_dir) # the image to be uploaded. Note: uploaded to school gallery directory
    uploaded_by = models.ForeignKey("SuperAdminPerson", on_delete=models.DO_NOTHING, related_name='school_images')
    is_approved = models.BooleanField(default=False) # this is so that students do have the opportunity to upload images
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class DisplayUser(models.Model):
    """
        This model determines if the user will be
        displayed on the about page of the school
        Note: the users should be restricted to administrators only
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey("AdminPerson", on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='displayed_users')
    is_displayed = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s displayed on %s" % (self.user, self.school)
