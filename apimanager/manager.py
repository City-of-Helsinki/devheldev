
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
    if hasattr(settings, "KONG_URL"):
        return kong.client.APIAdminClient('http://' + settings.KONG_URL + ':8001')
    else:
        raise ImproperlyConfigured('Kong installation URL is required')


def _kong_consumer_client():
    """
    If Kong URL is in settings, retuns a APIAdminClient instance configured
    there

    :return:kong.client.APIAdminClient
    """
    if hasattr(settings, "KONG_URL"):
        return kong.client.ConsumerAdminClient('http://' + settings.KONG_URL + ':8001')
    else:
        raise ImproperlyConfigured('Kong installation URL required')


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


def enable_file_logging(api_name, log_path=None):
    """

    :param api_name: Name or id of the API to enable file plugin for
    :param log_path: path where Kong should log API's events
    :return:
    """
    if not log_path:
        log_path = "/var/log/kong/{0}.log".format(api_name)

    return enable_plugin(api_name,
                         "file-log",
                         {"path": log_path})


def enable_rate_limiting(api_name,
                         **config):
    """
    Enables rate limiting plugin for given API with the following options

    Configuration arguments:
        consumer: Consumer ID or name, optional
        day:
        second:
        hour:
        month:
        year:
        async: asynchronous rate counter, default is False
        continue_on_error: whether to allow requests through when Kong database is down

    :param api_name: API name or ID
    :return: API specific plugin configuration id or None
    """

    return enable_plugin(api_name,
                         "rate-limiting",
                         {k: v for k, v in config.items() if v is not None or v is not ""})


def enable_ip_list(api_name, black=None, white=None, consumer_id=None):
    """
    Enable IP black or white lists for given API
    Either black or white needs to be truthy

    :param api_name: API name or ID
    :param black: comma separated string of IP addresses of CIDR ranges
    :param white: comma separated string of IP addresses of CIDR ranges
    :param consumer_id: optional, target specific consumer
    :return: API specific plugin configuration id or None
    """

    if not black or white:
        raise ValueError("Either black or white needs to have truthy value")

    config = {"config.blacklist": black,
              "config.white": white,
              "consumer_id": consumer_id}

    return enable_plugin(api_name,
                         "ip-restriction",
                         {k: v for k, v in config.items() if v is not None or v is not ""})
