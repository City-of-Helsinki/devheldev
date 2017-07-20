
from django.conf.urls import url

from .views import doc_view

urlpatterns = [
    url(r'(?P<path>.*)', doc_view, name='doc_view'),
]
