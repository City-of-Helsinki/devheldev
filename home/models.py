from __future__ import unicode_literals

from django.db import models
from django.utils.functional import cached_property

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

from apimanager.models import APIIndexPage
from projects.models import ProjectIndexPage
from blog.models import BlogIndexPage
from github.models import GithubOrgIndexPage
from aboutus.models import AboutUsIndexPage


class HomePage(Page):
    body = RichTextField(blank=True)
    template_name = models.CharField(max_length=50, null=True, blank=True)

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
        return GithubOrgIndexPage.objects.live().first()

    @cached_property
    def about_index(self):
        return AboutUsIndexPage.objects.live().first()

    def get_template(self, request, *args, **kwargs):
        if self.template_name:
            template = "%s/%s.html" % (self._meta.app_label, self.template_name)
            return template
        return super(HomePage, self).get_template(request, *args, **kwargs)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('template_name')
    ]
