
"""
API Management interface to Kong
"""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

import kong.client

# One place to store references to Kong plugin names
PLUGINS = {
    'key': 'key-auth'
}


def _kong_api_client():
    """
    If Kong URL is in settings, retuns a APIAdminClient instance configured
    there

    :return:kong.client.APIAdminClient
    """
    if settings.KONG_URL:
        return kong.client.APIAdminClient('http://' + settings.KONG_URL + ':8001')
    else:
        raise ImproperlyConfigured('Kong installation URL missing')


def _kong_consumer_client():
    """
    If Kong URL is in settings, retuns a APIAdminClient instance configured
    there

    :return:kong.client.APIAdminClient
    """
    if settings.KONG_URL:
        return kong.client.ConsumerAdminClient('http://' + settings.KONG_URL + ':8001')
    else:
        raise ImproperlyConfigured('Kong installation URL missing')


def get_api_count():
    """
    Returns amount of APIs in configured in Kong

    :return:int
    """

    kcli = _kong_api_client()
    return kcli.count()


def create_api(name, upstream_url, request_host=None, request_path=None,
               strip_request_path=False, preserve_host=False):
    """
    Create an API gateway

    :param name:short name for the API
    :param upstream_url:app_url of the API as an full URL
    :param request_host:host and domain API server is recognized by Kong (HTTP Host)
    :param request_path:part of the API path that Kong can use to recognize it
    :param strip_request_path:instruct Kong to remove request_path from upstream request
    :param preserve_host:instruct Kong to carry Host header to upstream server
    :return: Kong data
    """

    if not (request_host or request_path):
        raise ValueError

    kcli = _kong_api_client()

    if request_host:
        result = kcli.update(name, upstream_url=upstream_url,
                             request_host=request_host,
                             strip_request_path=str(strip_request_path),
                             preserve_host=str(preserve_host))
    else:
        result = kcli.update(name, upstream_url=upstream_url,
                             request_path=request_path,
                             strip_request_path=str(strip_request_path),
                             preserve_host=str(preserve_host))

    if result['id']:
        return result
    else:
        print(result)
        return False


def delete_api(name):
    """
    Remove API gateway

    :param name:short name of the API
    :return: Kong data
    """

    kcli = _kong_api_client()
    kcli.delete(name)


def update_api(api_id, name, upstream_url, request_host=None, request_path=None,
               strip_request_path=False, preserve_host=False):

    if not (request_host or request_path):
        raise ValueError

    kcli = _kong_api_client()

    if request_host:
        result = kcli.update(api_id, upstream_url=upstream_url, name=name,
                             request_host=request_host,
                             strip_request_path=str(strip_request_path),
                             preserve_host=str(preserve_host))
    else:
        result = kcli.update(api_id, upstream_url=upstream_url, name=name,
                             request_path=request_path,
                             strip_request_path=str(strip_request_path),
                             preserve_host=str(preserve_host))

    if result['id']:
        return result
    else:
        print(result)
        return False


def enable_plugin(name, plugin, options=None):
    """
    Enable given plugin for given API and set its options

    :param name: API name
    :param plugin: Kong Plugin name, eg. Key-Auth
    :param options: as Kong plugin requires
    :return:
    """
    if not options:
        options = {"enabled": True}

    kcli = _kong_api_client()
    plugin_conf = kcli.plugins(name)
    result = plugin_conf.create(plugin, **options)
    if result['api_id']:
        return result
    else:
        print(result)
        return None


def list_apis():
    """

    :return: Kong data
    """
    kcli = _kong_api_client()
    return kcli.list()


def check_api(name):
    kcli = _kong_api_client()
    apis = kcli.list()
    matching_api = [api for api in apis['data'] if api['name'] == name]
    if matching_api:
        return matching_api[0]
    else:
        return None


def add_consumer(username, custom_id=None):
    """
    Add a consumer to kong using either username or custom id

    :param username: username
    :param custom_id: custom id or Kong id
    :return: Kong data including created consumer's id
    """
    ucli = _kong_consumer_client()
    result = ucli.create(username, custom_id)
    if result['id']:
        return result
    else:
        return False


def delete_consumer(username, cid=None):
    """
    Delete consumer from Kong using given username or id

    :param username: username
    :param cid: custom id or Kong id
    :return: None (Kong API does not return anything)
    """
    ucli = _kong_consumer_client()
    try:
        ucli.delete(username or cid)
    except ValueError:
        pass


def get_consumer(username, cid=None):
    """
    Get consumer data from Kong

    :param username: username
    :param cid: Kong id
    :return: Consumer dat
    """
    ucli = _kong_consumer_client()
    try:
        res = ucli.retrieve(username or cid)
        return res
    except ValueError:
        return None


def list_consumers():
    """
    List consumers from Kong

    :return: Kong data
    """
    ucli = _kong_consumer_client()
    return ucli.list()


def request_api_key(consumer_id):
    """
    Request an API key for given consumer id

    :param consumer_id: Kong consumer id
    :return: API key
    """
    ucli = _kong_consumer_client()
    kcli = ucli.key_auth(consumer_id)
    result = kcli.create()
    if result['key']:
        return result
    else:
        print(result)
        return None


def delete_api_key(consumer_id, key):
    """
    Delete given API key belonging given consumer

    :param consumer_id: Kong consuemr id
    :param key: API key
    :return: None (Kong API does not return anything)
    """
    ucli = _kong_consumer_client()
    kcli = ucli.key_auth(consumer_id)
    try:
        kcli.delete(key)
    except ValueError:
        pass
