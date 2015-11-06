
from django.conf.urls import include, url

urlpatterns = (
    url(r'pre_login/$', 'apimanager.views.pre_login_view', name='pre_login'),
    url(r'add/$', 'apimanager.views.add_application', name='add_application'),
    url(r'update/(.*)/$', 'apimanager.views.update_application', name='update_application'),
    url(r'apps/$', 'apimanager.views.view_applications', name='view_applications'),
)
