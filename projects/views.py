import csv
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
from projects.models import ProjectIndexPage, ProjectPage
from django.db.models import ObjectDoesNotExist
import urllib.request

# Create your views here.


def piwik_data(request, piwik_id):
    try:
        data = ProjectPage.objects.get(piwik_id=piwik_id).piwik_data()
    except ValueError:
        data = None
    return HttpResponse(data)


def kpi_data(request, slug):
    try:
        data = ProjectPage.objects.get(slug=slug).kpi_data()
    except ValueError:
        data = None
    return HttpResponse(data)


def uptime_data(request, uptimerobot_name=None):
    uptimerobot_name = urllib.request.unquote(uptimerobot_name)
    try:
        data = ProjectPage.objects.get(uptimerobot_name=uptimerobot_name).uptime_data()
    except ObjectDoesNotExist:
        data = None
    return HttpResponse(data)


def cfapi_list(request):
    # Returns csv for Code for America project API
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'
    writer = csv.writer(response)
    writer.writerow(['name', 'description', 'link_url', 'code_url', 'tags', 'status'])
    for project in ProjectIndexPage.objects.all()[0].projects():
        writer.writerow([project.title,
                         project.short_description,
                         project.links.filter(type='main').first().url if project.links.filter(type='main') else None,
                         project.links.filter(type='github').first().url if project.links.filter(type='github') else None,
                         ", ".join(tag.name for tag in project.tags.all())
                         if project.tags.all() else None,
                         project.status])
    return response
