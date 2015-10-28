import json, requests
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page, Orderable
import django.utils.dateparse as dateparse
from django.db import models


class GithubOrgIndexPage(Page):
    api_url = models.URLField(default='https://api.github.com/orgs/City-of-Helsinki/events?per_page=5')

    content_panels = Page.content_panels + [
        FieldPanel('api_url'),
     ]

    def events(self):
        response = requests.get(self.api_url)
        events = response.json()
        for index, event in enumerate(events):
            events[index]['created_at'] = dateparse.parse_datetime(event['created_at'])
        return events
