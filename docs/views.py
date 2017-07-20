
from pathlib import Path

from django.shortcuts import render
from django.utils.text import get_valid_filename
from django.conf import settings
from django.http import HttpResponseBadRequest, Http404


DOCS_STORAGE = Path(settings.BASE_DIR) / 'docs' / 'templates' / 'docs'


def validate_path_root(path, root=DOCS_STORAGE):
    """
    Checks whether given path is subpath of given root path

    :param path:Pathlib.Path instance
    :param root:Pathlib.Path instance
    :return: bool
    """
    return root not in path.parents


def doc_view(request, path, doc_root=DOCS_STORAGE):

    doc_path = doc_root / path

    if not validate_path_root(doc_path, doc_root):
        return HttpResponseBadRequest('Invalid path given for doc')

    if not path.exists():
        return Http404('No doc found for given path')

    return render(request, template_name=path, context={})
