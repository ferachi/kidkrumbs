from django.db.models.signals import post_save
from django.dispatch import receiver
from crumbs.models import Person
from crumbs.utils.image_editor import crop_image

@receiver(post_save, sender=Person)
def modify_person_avatar(sender,instance, **kwargs):
    if instance.avatar:
        # crop avatar to 1:1
        crop_image(instance.avatar,1)

