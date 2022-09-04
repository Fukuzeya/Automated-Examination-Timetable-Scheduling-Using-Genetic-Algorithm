from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Codes

@receiver(post_save, sender = User)
def post_save_generate_code(sender,instance, created, *args, **kwargs):
    if created:
        Codes.objects.create(user=instance)
