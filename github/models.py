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

    max_amount = 40

    def events(self, amount=max_amount):
        try:
            events = cache.get('github')
            if not events:
                response = requests.get('https://api.github.com/orgs/' + self.github_org_name + '/events?per_page=' + str(self.max_amount))
                if response.status_code == 200:
                    events = response.json()
                    for index, event in enumerate(events):
                        # event['created_at'] = dateparse.parse_datetime(event['created_at'])
                        # get html repo url
                        event['repo']['url'] = event['repo']['url'].replace('https://api.github.com/repos/', 'https://github.com/')
                    cache.add('github', events, 60)
            events = cache.get('github')
            return json.dumps(events[:amount])
        except (TypeError, KeyError):
            # not enough events
            return None
