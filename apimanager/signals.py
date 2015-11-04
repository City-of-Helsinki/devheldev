
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import APISubscription

@receiver(post_save, sender=APISubscription)
def handle_subscription_save(sender, **kwargs):
    print("Sub saved!")

