
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


def create_api(name, upstream_url, request_host):
    """
    Create an API gateway

    :param name:short name for the API
    :param upstream_url:location of the API as an full URL
    :param request_host:host and domain API server is recognized by Kong (HTTP Host)
    :return: Kong data
    """

    kcli = _kong_api_client()
    result = kcli.create(upstream_url=upstream_url, name=name, request_host=request_host)
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


def update_api(api_id, **kwargs):
    kcli = _kong_api_client()
    result = kcli.update(api_id, **kwargs)
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
    matching_api = [api for api in apis['data'] if api['name'] is name]
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


def delete_consumer(username, cid):
    """
    Delete consumer from Kong using given username or id

    :param username: username
    :param cid: custom id or Kong id
    :return: None (Kong API does not return anything)
    """
    ucli = _kong_consumer_client()
    ucli.delete(username or cid)


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


def delete_api_key(consumer_id, key_id):
    """
    Delete API key

    :param consumer_id: Kong consumer id
    :param key_id: Kong Key id
    :return: None
    """

    ucli = _kong_consumer_client()
    kcli = ucli.key_auth(consumer_id)
    kcli.delete(key_id)


def delete_api_key(consumer_id, key):
    """
    Delete given API key belonging given consumer

    :param consumer_id: Kong consuemr id
    :param key: API key
    :return: None (Kong API does not return anything)
    """
    ucli = _kong_consumer_client()
    kcli = ucli.key_auth(consumer_id)
    kcli.delete(key)

