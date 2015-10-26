from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailsearch import index
from wagtail.wagtailadmin.edit_handlers import FieldPanel

# Create your models here.


class PersonPage(Orderable, Page):
    name = models.CharField(max_length=200, null=False)
    contact = models.URLField(null=False)
    photo = models.ImageField(upload_to='aboutus_images', blank=True, null=True)
    job_title = models.CharField(max_length=20)
    description = models.CharField(max_length=200, blank=True, null=True)
    listed = models.BooleanField()

    search_fields = Page.search_fields + (
        index.SearchField('name'),
        index.SearchField('job_title'),
        index.SearchField('description'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('contact'),
        FieldPanel('photo'),
        FieldPanel('job_title'),
        FieldPanel('description'),
        FieldPanel('listed')
    ]


class AboutUsIndexPage(Page):

    def people(self):
        return PersonPage.objects.live().filter(listed=True)
