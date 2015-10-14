from django.db import models


from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class APIPage(Page):
    name = models.CharField(max_length=300, blank=False, null=False)
    location = models.URLField(blank=False, null=False)
    documentation = models.URLField(blank=True)
    short_description = models.TextField(blank=False)
    full_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('location'),
        FieldPanel('documentation'),
        FieldPanel('short_description', classname="full"),
        FieldPanel('full_description', classname="full")
    ]

