import json, requests
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page, Orderable
import django.utils.dateparse as dateparse
from django.db import models
from django.core.cache import cache


class GithubOrgIndexPage(Page):
    github_org_name = models.CharField(default='City-of-Helsinki', max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('github_org_name'),
     ]

    def events(self):
        events = cache.get('events')
        if not events:
            cache.add('events',
                               requests.get('https://api.github.com/orgs/' + self.github_org_name + '/events?per_page=20').json(), 60)
            events = cache.get('events')
        for index, event in enumerate(events):
            events[index]['created_at'] = dateparse.parse_datetime(event['created_at'])
        return events

    def top_events(self):
        return self.events()[:3]
