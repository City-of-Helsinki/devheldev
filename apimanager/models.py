from django.db import models


from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index

class APIPage(Orderable, Page):
    name = models.CharField(max_length=300, blank=False, null=False)
    api_path = models.CharField("Root path for API Management platform", max_length=50, default="",
                                help_text="User visible path; example usage: api.hel.fi/{path}/")
    location = models.URLField(blank=False, null=False)
    documentation = models.URLField(blank=True)
    short_description = models.TextField(blank=False)
    full_description = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('name'),
        index.SearchField('location'),
        index.SearchField('short_description'),
        index.SearchField('full_description'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('location'),
        FieldPanel('documentation'),
        FieldPanel('short_description', classname="full"),
        FieldPanel('full_description', classname="full")
    ]


class APIIndexPage(Page):
    subpage_types = ['apimanager.ApiPage']

    def apis(self):
        return APIPage.objects.live()


class KongAPIConfiguration(models.Model):
    api_page = models.OneToOneField(APIPage)
    request_host = models.CharField('Hostname for API management platform', max_length=150,
                                    default="api.hel.fi",
                                    help_text="Similar to HTTP virtual hosts; changing this from default is required if user visible API host is publicly different")
    kong_api_id = models.CharField(max_length=300, editable=False, null=True)

    def __str__(self):
        return u'Configuration for ' + self.api_page.name


from django.conf import settings
from . import manager

class Application(models.Model):
    """
    Individual application for the API customer
    containing one Kong consumer and its API key
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    subscriptions = models.ManyToManyField(KongAPIConfiguration, through='APISubscription')
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    location = models.URLField(blank=True, null=True)

    def __str__(self):
        return u'Application of ' + self.user.username


class APISubscription(models.Model):
    api = models.ForeignKey(KongAPIConfiguration)
    application = models.ForeignKey(Application)
    consumer_id = models.CharField(max_length=300, blank=True, null=True)
    consumer_kong_id = models.CharField(max_length=300, blank=True, null=True)
    key = models.CharField(max_length=300, blank=True, null=True)
    key_kong_id = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return u'API subscription for ' + self.api.api_page.name

    def add_consumer(self):
        """
        Add consumer to Kong for this APISubscription using username
        and subscription id
        """
        res = manager.add_consumer(self.application.user.username + '_' + str(self.pk))
        if res:
            self.consumer_kong_id = res['id']
            self.save()

    def get_api_key(self):
        """
        Register API key in Kong for this subscription using
        its consumer id
        """
        res = manager.request_api_key(self.consumer_kong_id)
        if res:
            self.key = res['key']
            self.key_kong_id = res['id']
            self.save()
