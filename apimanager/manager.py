
"""
API Management interface to Kong
"""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

import kong.client


def _kong_client():
    """
    If Kong URL is in settings, retuns a APIAdminClient instance configured
    there

    :return:kong.client.APIAdminClient
    """
    if settings.KONG_URL:
        return kong.client.APIAdminClient('http://' + settings.KONG_URL)
    else:
        raise ImproperlyConfigured('Kong installation URL missing')


def get_api_count():
    """
    Returns amount of APIs in configured in Kong

    :return:int
    """

    kcli = _kong_client()
    return kcli.count()


def create_api(name, upstream_url, request_host):
    """
    Create an API gateway

    :param name:short name for the API
    :param upstream_url:location of the API as an full URL
    :param request_host:host and domain API server is recognized by Kong (HTTP Host)
    :return:
    """

    kcli = _kong_client()
    result = kcli.create(upstream_url=upstream_url, name=name, request_host=request_host)
    if result['id']:
        return True
    else:
        return False


def remove_api(name):
    """
    Remove API gateway

    :param name:short name of the API
    :return:None
    """

    kcli = _kong_client()
    kcli.delete(name)

