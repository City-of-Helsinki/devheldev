from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
from projects.models import ProjectPage
import urllib.request

# Create your views here.


def piwik_data(request, piwik_id):
    data = ProjectPage.objects.get(piwik_id=piwik_id).piwik_data()
    return HttpResponse(data)


def uptime_data(request, uptimerobot_name):
    uptimerobot_name = urllib.request.unquote(uptimerobot_name)
    data = ProjectPage.objects.get(uptimerobot_name=uptimerobot_name).uptime_data()
    return HttpResponse(data)
