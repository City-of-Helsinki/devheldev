import blog
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from django.shortcuts import redirect
from django.conf import settings

import projects.views
import github.views

def redirect_to_sso(request):
    """
    Bypass traditional Django login by redirecting to SSO server
    If GET has next argument, that will be added to redirect

    :param request: Django request
    :return: HttpResponseRedirect
    """

    if request.GET.get('next'):
        sso_url = settings.AUTH_SSO_URL + '&next={}'.format(request.GET.get('next'))
    else:
        sso_url = settings.AUTH_SSO_URL

    return redirect(sso_url)

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^accounts/login/$', redirect_to_sso, name='redirect_to_sso'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^search/$', 'search.views.search', name='search'),
    url(r'^api/', include('apimanager.urls', namespace="apimanager")),
    # client endpoints for external API data
    url(r'^piwik_data/(.*)/', projects.views.piwik_data),
    url(r'^uptime_data/(.*)/', projects.views.uptime_data),
    url(r'^github_data/', github.views.github_data),
    # wagtail handles the rest
    url(r'', include(wagtail_urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
