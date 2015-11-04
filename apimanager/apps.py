
from django.apps import AppConfig


class APIManagerConfig(AppConfig):

    name = 'apimanager'
    verbose_name = "for managing API gateway Kong"

    def ready(self):
        print("importing")
        import apimanager.signals
        print("imported", apimanager.signals.handle_subscription_save)

