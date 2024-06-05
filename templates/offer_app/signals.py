from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import TagOfferModel


@receiver(post_migrate)
def create_initial_skills(sender, **kwargs):
    if sender.name == 'client':
        initial_tags = ['MP4', 'MOV', 'Wedding Videography', 'Graphic Design', 'Telegram bot', 'WebSite']
        for tag_name in initial_tags:
            TagOfferModel.objects.get_or_create(name=tag_name)
