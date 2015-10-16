from django.db import models


from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index

class APIPage(Orderable, Page):
    name = models.CharField(max_length=300, blank=False, null=False)
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
