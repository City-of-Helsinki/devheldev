import json, requests
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page, Orderable
import django.utils.dateparse as dateparse
from django.db import models


class GithubOrgIndexPage(Page):
    github_org_name = models.CharField(default='City-of-Helsinki', max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('github_org_name'),
     ]

    def events(self):
        response = requests.get('https://api.github.com/orgs/' + self.github_org_name + '/events?per_page=5')
        events = response.json()
        for index, event in enumerate(events):
            events[index]['created_at'] = dateparse.parse_datetime(event['created_at'])
        return events
