# -*- coding: utf-8 -*-
import pytest
from home.models import HomePage


@pytest.mark.django_db
@pytest.fixture
def home_page():
    return HomePage.objects.create(title='Test Home')

