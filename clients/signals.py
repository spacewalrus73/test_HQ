from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from clients.models import Client


@receiver(signal=post_save, sender=User)
def post_save_create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user=instance)
