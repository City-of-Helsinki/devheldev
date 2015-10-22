import json, requests
from wagtail.wagtailcore.models import Page, Orderable
import django.utils.dateparse as dateparse

class GithubIndexPage(Page):

    def events(self):
        url = "https://api.github.com/orgs/City-of-Helsinki/events?per_page=5"
        response = requests.get(url)
        events = response.json()
        for index, event in enumerate(events):
            events[index]['created_at'] = dateparse.parse_datetime(event['created_at'])
        return events
