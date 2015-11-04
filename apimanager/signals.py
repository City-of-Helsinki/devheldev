
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import APISubscription


@receiver(post_save, sender=APISubscription)
def handle_subscription_save(sender, **kwargs):
    sub = kwargs.get('instance')
    if sub:
        if not sub.consumer_kong_id:
            sub.add_consumer()
        sub.get_api_key()


@receiver(post_delete, sender=APISubscription)
def handle_subscription_delete(sender, **kwargs):
    sub = kwargs.get('instance')
    if sub:
        if sub.consumer_kong_id:
            sub.delete_consumer()
            sub.delete_api_key()

