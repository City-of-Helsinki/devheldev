from django.db import models
from django.conf import settings
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from . import manager


class APIPage(Orderable, Page):
    name = models.CharField("Short and unique identifier for API", max_length=300, blank=False, null=False, unique=True)
    use_api_gateway = models.BooleanField(default=False, help_text="Set to false for APIs not managed by the api.hel.fi API gateway.")
    api_path = models.CharField("Root path for API Management platform", max_length=50, default="", blank=True, null=True,
                                help_text="Actual public API root endpoint; example usage: api.hel.fi/{path}/")
    api_url = models.URLField(blank=False, null=False)
    documentation = models.URLField(blank=True)
    short_description = models.TextField(blank=False)
    full_description = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    search_fields = Page.search_fields + (
        index.SearchField('name'),
        index.SearchField('api_url'),
        index.SearchField('short_description'),
        index.SearchField('full_description'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('api_url'),
        FieldPanel('use_api_gateway'),
        FieldPanel('api_path'),
        FieldPanel('documentation'),
        ImageChooserPanel('image'),
        FieldPanel('short_description', classname="full"),
        FieldPanel('full_description', classname="full")
    ]


class APIIndexPage(Page):
    subpage_types = ['apimanager.ApiPage']

    def apis(self):
        return APIPage.objects.live()


class KongAPIConfiguration(models.Model):
    api_page = models.OneToOneField(APIPage)
    request_host = models.CharField('Host and domain name', max_length=150,
                                    unique=True,
                                    help_text="Kong requires that API has a unique host name,"
                                              " f.x. name.api.hel.fi -> api.hel.fi/name")
    kong_api_id = models.CharField(max_length=300, editable=False, null=True)

    def __str__(self):
        return u'Configuration for ' + self.api_page.name

    def save_to_kong(self, enable_key_auth=False):
        """
        Create or update API configuration in Kong

        :param enable_key_auth: to enable key auth for API
        :type enable_key_auth: str
        :return: None
        :rtype: None
        """
        existing = manager.check_api(self.api_page.name)
        if existing:
            res = manager.update_api(api_id=self.kong_api_id,
                                     upstream_url=self.api_page.api_path,
                                     request_host=self.request_host)
        else:
            res = manager.create_api(name=self.api_page.name,
                                     upstream_url=self.api_page.api_path,
                                     request_host=self.request_host)
            self.kong_api_id = res['id']
            self.save()

        if enable_key_auth:
            manager.enable_plugin(self.api_page.name, manager.PLUGINS['key'])


class Application(models.Model):
    """
    Individual application for the API customer
    containing one Kong consumer and its API key
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    subscriptions = models.ManyToManyField(KongAPIConfiguration, through='APISubscription')
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    app_url = models.URLField(blank=True, null=True)

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
        if self.consumer_kong_id:
            consumer = manager.get_consumer(self.consumer_kong_id)
            if consumer:
                return True
        res = manager.add_consumer(self.application.user.username + '_' + str(self.pk))
        if res:
            self.consumer_kong_id = res['id']
            self.save()
        return True

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

    def delete_consumer(self):
        """
        Delete subscription's Consumer from Kong
        :return: None
        """
        manager.delete_consumer(cid=self.consumer_kong_id)
        self.consumer_kong_id = None
        self.save()

    def delete_api_key(self):
        """
        Delete API key from Kong
        :return: None
        """
        manager.delete_api_key(self.consumer_kong_id, self.key_kong_id)
        self.key = False
        self.key_kong_id = False
        self.save()

