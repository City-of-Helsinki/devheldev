import json, requests
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailcore.models import Page, Orderable
from django.db import models
from django.core.cache import cache
from django.conf import settings
import django.utils.dateparse as dateparse
from datetime import datetime
import pytz


class EventsIndexPage(Page):
    facebook_page_id = models.CharField(default='1415745085336451', max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('facebook_page_id'),
     ]

    def events(self):
        if not hasattr(settings, 'FACEBOOK_APP_ID') or not hasattr(settings, 'FACEBOOK_APP_SECRET'):
            return []
        events = cache.get('facebook')
        try:
            if not events:
                events = []
                feed = requests.get('https://graph.facebook.com/v2.5/' +
                                    self.facebook_page_id +
                                    '?fields=feed{link,message,object_id}' +
                                    '&access_token=' +
                                    str(settings.FACEBOOK_APP_ID) + '|' +
                                    settings.FACEBOOK_APP_SECRET).json()['feed']['data']

                # filter the events from the feed

                for item in feed:
                    if 'link' in item:
                        if 'events' in str(item['link']):
                            events.append(item)

                # fetch details for the events

                event_ids = ','.join([event['object_id'] for event in events])
                details = []
                details = requests.get('https://graph.facebook.com/v2.5/?ids=' +
                                    event_ids +
                                    '&fields=description,cover,end_time,name,start_time,id,picture,place' +
                                    '&access_token=' +
                                    str(settings.FACEBOOK_APP_ID) + '|' +
                                    settings.FACEBOOK_APP_SECRET).json()
                for index, detail in details.items():
                    detail['start_time'] = dateparse.parse_datetime(detail['start_time'])
                    detail['end_time'] = dateparse.parse_datetime(detail['end_time'])
                    # TODO: implement geocoding of event location
                for event in events:
                    event['details'] = details[event['object_id']]
                cache.add('facebook', events, 3600)
        except LookupError:
            # in case facebook API doesn't return proper data
            return []
        return events

    def future_events(self):
        tz = pytz.timezone(settings.LOCAL_TIME_ZONE)
        # we want the next event first
        return reversed([event for event in self.events() if event['details']['end_time'] > datetime.now(tz)])
