import json, requests
from wagtail.wagtailcore.models import Page, Orderable

class GithubIndexPage(Page):

    def events(self):
        url = "https://api.github.com/orgs/City-of-Helsinki/events?per_page=5"
        response = requests.get(url)
        events = response.json()
        return events
