from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response

# Create your views here.


def project_view(request, template='project_page.html'):
    context = {'piwik_url': settings.PIWIK_URL}
    return render_to_response(template, context)