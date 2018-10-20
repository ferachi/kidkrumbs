from django.utils.text import slugify

def upload_school_logo_dir(instance, filename):
    name = slugify(instance.name)
    school = instance.slug
    extension = filename.split('.')[-1]
    new_filename = "{0}-logo.{1}".format(name, extension)
    return "schools/%s/logos/%s" % (school, new_filename)

def upload_school_images_dir(instance, filename):
    school = instance.slug
    name = slugify(instance.name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "schools/%s/images/%s" % (school, new_filename)

def upload_school_gallery_dir(instance, filename):
    school = instance.gallery.school.slug
    name = slugify(instance.title)
    gallery = slugify(instance.gallery.name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "schools/%s/galleries/%s/%s" % (school, gallery,new_filename)

def upload_subject_avatars_dir(instance, filename):
    name = slugify(instance.subject_code)
    subject = slugify(instance.base_subject)
    school = slugify(instance.base_subject.school.name)
    base, extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "schools/%s/subjects/%s/avatars/%s" % (school,subject, new_filename)


def upload_person_avatars_dir(instance, filename):
    name = slugify(instance.full_name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "people/avatar/%s/%s" % (name, new_filename)


def upload_person_images_dir(instance, filename):
    name = slugify(instance.full_name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "people/passport/%s/%s" % (name, new_filename)

    
def upload_group_gallery_dir(instance, filename):
    title = slugify(instance.title)
    name = instance.gallery.group.slug
    gallery = slugify(instance.gallery.name)
    school = slugify(instance.gallery.group.school.name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(title, extension)
    return "schools/%s/groups/%s/galleries/%s/%s" % (school, name,gallery, new_filename)


def upload_group_avatars_dir(instance, filename):
    name = instance.slug
    school = slugify(instance.session.school.name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "schools/%s/groups/%s/avatars/%s" % (school, name, new_filename)


def upload_blog_images_dir(instance, filename):
    name = slugify(instance.title)
    school = slugify(instance.term.session.school.short_name)
    session = instance.term.session.slug
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "schools/%s/%s/blogs/images/%s" % (school, session, new_filename)

def school_events_images_dir(instance, filename):
    name = instance.title
    slug = slugify(name)
    session = instance.term.session.slug
    school = slugify(instance.term.session.school.short_name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(name, extension)
    return "schools/%s/%s/events/images/%s" % (school, session, new_filename)


def upload_assessment(instance, filename):
    name = "{} {} {}".format(instance.assessment.course.course_code, instance.assessment.assessment_type.name, instance.classroom.slogan)
    slug = slugify(name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(slug, extension)
    return "assessments/%s/%s/%s/%s/%s" % (slugify(instance.assessment.term.session.session_year), slugify(instance.assessment.term.name),
                                  slugify(instance.classroom.slogan), instance.assessment.assessment_type.name, new_filename)


def upload_assessment_results(instance, filename):
    name = "{} {}".format(instance.enrollment.student, instance.assessement.assessement_type)
    slug = slugify(name)
    extension = filename.split('.')[-1]
    new_filename = "{0}.{1}".format(slug, extension)
    return "assessment_results/%s/%s/%s/%s" % (instance.term.session.session_year, instance.term.name,
                                  instance.assessement.assessement_type, new_filename)
