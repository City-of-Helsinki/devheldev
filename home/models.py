from __future__ import unicode_literals

from django.db import models
from django.utils.functional import cached_property

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from apimanager.models import APIIndexPage
from projects.models import ProjectIndexPage
from blog.models import BlogIndexPage
from github.models import GithubIndexPage


class HomePage(Page):
    body = RichTextField(blank=True)

    @cached_property
    def blog_index(self):
        return BlogIndexPage.objects.live().first()

    @cached_property
    def project_index(self):
        return ProjectIndexPage.objects.live().first()

    @cached_property
    def api_index(self):
        return APIIndexPage.objects.live().first()

    @cached_property
    def commit_index(self):
        return GithubIndexPage.objects.live().first()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]
