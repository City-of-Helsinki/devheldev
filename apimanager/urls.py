
from django.conf.urls import include, url

urlpatterns = (
    url(r'add/$', 'apimanager.views.add_application', name='add_application'),
)
