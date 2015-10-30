
from django.contrib import admin
from .models import KongAPIConfiguration, Application, APISubscription

admin.site.register(KongAPIConfiguration)
admin.site.register(Application)
admin.site.register(APISubscription)
