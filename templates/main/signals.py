from django.db.models.signals import post_save, pre_save, post_migrate
from django.dispatch import receiver
from .models import MyUser
from PIL import Image
import random
import string


@receiver(post_save, sender=MyUser)
def resize_image(sender, instance, created, **kwargs):
    image_field = instance.image
    if image_field:
        img = Image.open(image_field.path)
        img.thumbnail((69, 69))
        img.save(image_field.path)

@receiver(pre_save, sender=MyUser)
def generate_unique_key(sender, instance, **kwargs):
    if not instance.user_id_key:
        unique_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        instance.user_id_key = unique_key