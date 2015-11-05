# -*- coding: utf-8 -*-
from blog.models import BlogIndexPage
import pytest
from apimanager.models import APIIndexPage
from github.models import GithubOrgIndexPage
from home.models import HomePage
from events.models import EventsIndexPage
from aboutus.models import AboutUsIndexPage
from wagtail.wagtailcore.models import Page
from projects.models import ProjectIndexPage


def root_page():
    return Page.objects.get(depth=1)


@pytest.mark.django_db
@pytest.fixture
def home_page():
    return root_page().add_child(instance=HomePage(title='Test Home', live=True))


@pytest.mark.django_db
@pytest.fixture
def index_pages():
    home = home_page()
    events_index = home.add_child(instance=EventsIndexPage(title='Test Events Index', live=True))
    about_index = home.add_child(instance=AboutUsIndexPage(title='Test About Index', live=True))
    github_index = home.add_child(instance=GithubOrgIndexPage(title='Test Github Index', live=True))
    project_index = home.add_child(instance=ProjectIndexPage(title='Test Project Index', live=True))
    api_index = home.add_child(instance=APIIndexPage(title='Test API Index', live=True))
    blog_index = home.add_child(instance=BlogIndexPage(title='Test Blog Index', live=True))

    return [home, events_index, about_index, github_index, project_index, api_index, blog_index]
