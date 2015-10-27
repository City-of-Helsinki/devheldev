
from django.conf.urls import include, url

urlpatterns = (
    url(r'add/$', 'apimanager.views.add_application', name='add_application'),
    url(r'apps/$', 'apimanager.views.view_applications', name='view_applications')
)
