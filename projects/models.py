from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from modelcluster.fields import ParentalKey


class ProjectPage(Orderable, Page):
    STATUSES = (
        ('discovery', 'Discovery'),
        ('alpha', 'Alpha'),
        ('beta', 'Beta'),
        ('live', 'LIVE')
    )
    short_description = models.TextField()
    full_description = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    status = models.CharField(max_length=20, choices=STATUSES, default='discovery')
    def save(self, *args, **kwargs):
        if not self.title:
            if self.project:
                self.title = self.project.name
        return super().save(*args, **kwargs)

    search_fields = Page.search_fields + (
        index.SearchField('short_description'),
        index.SearchField('full_description'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('status'),
        FieldPanel('short_description'),
        FieldPanel('full_description'),
        ImageChooserPanel('image'),
        InlinePanel('kpis', label="Key performance indicators"),
        InlinePanel('roles', label="Contact us"),
        InlinePanel('links', label="Links"),
    ]


class ProjectRole(models.Model):
    TYPES = (
        ('owner', 'Product owner'),
        ('tech', 'Tech lead'),
    )
    project = ParentalKey('projects.ProjectPage', related_name='roles')
    type = models.CharField(max_length=20, choices=TYPES)
    person = ParentalKey('aboutus.PersonPage', related_name='roles')


class ProjectKPI(models.Model):
    project = ParentalKey('projects.ProjectPage', related_name='kpis')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200, null=True, blank=True)
    value = models.CharField(max_length=200)


class ProjectLink(models.Model):
    TYPES = (
        ('main', 'Main'),
        ('github', 'GitHub'),
    )

    project = ParentalKey('projects.ProjectPage', related_name='links')
    type = models.CharField(max_length=20, choices=TYPES)
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return "{0} / {1}".format(str(self.project), self.type)


class ProjectIndexPage(Page):
    subpage_types = ['projects.ProjectPage']

    def projects(self):
        return ProjectPage.objects.live()

    def top_projects(self):
        return self.projects()[:5]
