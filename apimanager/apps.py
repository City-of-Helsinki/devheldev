
from django.apps import AppConfig


class APIManagerConfig(AppConfig):

    name = 'apimanager'
    verbose_name = "for managing API gateway Kong"

    def ready(self):
        import apimanager.signals
