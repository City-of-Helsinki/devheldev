from django.shortcuts import render
from django.http import HttpResponse
from events.models import EventsIndexPage

# Create your views here.


def event_data(request):
    future = request.GET.get('future', 'False')
    if future.lower() == 'True'.lower():
        data = EventsIndexPage.objects.get().events(future=True)
    else:
        data = EventsIndexPage.objects.get().events()
    return HttpResponse(data)
