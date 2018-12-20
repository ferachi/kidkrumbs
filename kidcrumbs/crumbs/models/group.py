from django.db import models
from django.utils.text import slugify
from crumbs.utils.colors import COLORS
from crumbs.utils.image_uploaders import upload_group_gallery_dir, upload_group_avatars_dir
from django.urls import reverse
import uuid

class AbstractGroup(models.Model):
    CATEGORIES = (
        ('SH', 'school house'),
        ('SP', 'sports'),
        ('MS', 'music'),
        ('LT', 'literature'),
        ('SC', 'science'),
        ('AR', 'arts'),
        ('CR', 'classroom'),
        ('CL', 'class'),
        ('DP', 'department'),
        ('OT', 'others')
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=2, choices=CATEGORIES)
    school = models.ForeignKey('School',related_name="%(class)s", on_delete = models.CASCADE) # little issue here for base class and classroom.(reflected twice)
    created_by = models.ForeignKey("AdminPerson", related_name="created_%(class)s", on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name', '-created_date']



# The Group class is to act like an abstract model in a sense.
# however it is not. This is done intentionally to allow a single
# query request for all group subclasses. 
# This class does not have a school but it does have a session where
# the school can be found
# NOTE: All Group subclasses must have (composite) a class that subclasses
# the AbstractGroup as a foreignkey field.

class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(blank=True)
    slogan = models.CharField(max_length=100, blank=True)
    overview = models.TextField()
    tags = models.CharField(max_length=150, help_text="Specify keywords that can be used to identify this group followed by commas.")
    avatar = models.ImageField(upload_to=upload_group_avatars_dir, null=True, blank=True)
    color = models.CharField(max_length=20, choices=COLORS, default='DODGERBLUE')
    members = models.ManyToManyField('Person', through='Membership', related_name='group_list')
    habits = models.ManyToManyField('Habit', related_name='groups', blank=True)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
    created_by = models.ForeignKey("AdminPerson", related_name="created_groups", on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return self.slug

    def __str__(self):
        return self.full_name
    
    def __repr__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        super(Group, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    # 	return reverse('crumbs:groups:group_detail', kwargs={'slug': self.slug})


class GroupComment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    group = models.ForeignKey('Group', related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']


    def __str__(self):
        return "{0} comment at {1}".format(self.person.full_name, self.created_date.strftime("%c"))


class GroupGallery(models.Model):
    """
    The Group Gallery Model
    On the main application, this will serve as an Album for each group
    This is applicable to only the platinium and gold plans
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='galleries')
    name = models.CharField(max_length=50) # name of the album
    description = models.TextField(null=True, blank=True) # a brief description
    created_date = models.DateTimeField(auto_now_add=True) # day this album is created
    timestamp = models.DateTimeField(auto_now=True) # for the updates in the future
    created_by = models.ForeignKey("AdminPerson",on_delete=models.DO_NOTHING, related_name='galleries')
    max_num_images = models.PositiveSmallIntegerField(default=20, editable=False) # maximum number of images per gallery
    is_public = models.BooleanField(default=False) # can this gallery be shown to the public (external people)
    def __str__(self):
        return "%s %s" %( self.name, "album")


class GroupImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gallery = models.ForeignKey('GroupGallery', on_delete=models.CASCADE, related_name='images')
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_group_gallery_dir)
    uploaded_by = models.ForeignKey("AdminPerson", on_delete=models.DO_NOTHING, related_name='group_images')
    created_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False) # this is so that students do have the opportunity to upload images

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_date','title')

