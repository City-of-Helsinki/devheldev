# -*- coding: utf-8 -*-
import pytest
from home.models import HomePage
from events.models import EventsIndexPage
from aboutus.models import AboutUsIndexPage
from wagtail.wagtailcore.models import Page


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

    return [home, events_index, about_index]
