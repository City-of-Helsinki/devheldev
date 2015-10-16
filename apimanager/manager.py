
"""
API Management interface to Kong
"""

from django.conf import settings

import kong.client


def get_api_count():
    kcli = kong.client.APIAdminClient('http://' + settings.KONG_URL)
    return kcli.count()


def create_api(name, upstream_url, request_host):
    kcli = kong.client.APIAdminClient('http://' + settings.KONG_URL)
    result = kcli.create(upstream_url=upstream_url, name=name, request_host=request_host)
    if result['id']:
        return True
    else:
        return False


def remove_api(name):
    kcli = kong.client.APIAdminClient('http://' + settings.KONG_URL)
    kcli.delete(name)

