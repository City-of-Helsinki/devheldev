from django.db import models
from django.conf import settings

import datetime

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

class InfoPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
    ])

InfoPage.content_panels = Page.content_panels + [
    StreamFieldPanel('body'),
]
