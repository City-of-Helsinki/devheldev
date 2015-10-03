from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailsearch import index


class Project(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField()
    full_description = RichTextField(blank=True)

    def __str__(self):
        return self.name


class ProjectLink(models.Model):
    TYPES = (
        ('main', 'Main'),
        ('github', 'GitHub'),
    )

    project = models.ForeignKey(Project)
    type = models.CharField(max_length=20, choices=TYPES)
    description = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return "{0} / {1}".format(str(self.project), self.type)


class ProjectPage(Page):
    project = models.OneToOneField(Project, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.title:
            if self.project:
                self.title = self.project.name
        return super().save(*args, **kwargs)

    search_fields = Page.search_fields + (
        index.SearchField('project__name'),
        index.SearchField('project__short_description'),
        index.SearchField('project__long_description'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('project'),
    ]


class ProjectIndexPage(Page):
    subpage_types = ['projects.ProjectPage']
