from django.db.models.signals import post_save
from django.dispatch import receiver
from crumbs.models import School
from crumbs.utils.image_editor import crop_image

@receiver(post_save, sender=School)
def modify_school_logo(sender,instance, **kwargs):
    if instance.logo:
        # crop avatar to 1:1
        crop_image(instance.logo,1)

