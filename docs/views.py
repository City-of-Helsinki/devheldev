
from pathlib import Path

from django.shortcuts import render
from django.utils.text import get_valid_filename
from django.conf import settings
from django.http import HttpResponseBadRequest, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse


DOCS_STORAGE = Path(settings.BASE_DIR) / 'docs' / 'templates' / 'docs'
DOCS_TEMPLATE_ROOT = Path('docs')


def validate_path_root(path, root=DOCS_STORAGE):
    """
    Checks whether given path is subpath of given root path

    :param path:Pathlib.Path instance
    :param root:Pathlib.Path instance
    :return: bool
    """
    return root not in path.parents


def doc_view(request, path, doc_root=DOCS_STORAGE):

    if path == '':
        index_page = reverse('doc_view', kwargs={'path': 'README/'})
        return HttpResponseRedirect(index_page)

    doc_path = doc_root / path
    doc_path = doc_path.absolute()

    if validate_path_root(doc_path, doc_root):
        return HttpResponseBadRequest('Invalid path given for doc')

    if not doc_path.exists():
        raise Http404('No doc found for given path')

    doc_as_template_path = DOCS_TEMPLATE_ROOT / path

    if doc_path.is_dir():
        doc_as_template_path = doc_as_template_path / 'index.html'

    elif not doc_path.suffix == '.html':
        return HttpResponseBadRequest('Bad file request')

    return render(request, template_name=doc_as_template_path, context={})
