
import json
import logging
from collections import namedtuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

APIEndpoint = namedtuple("APIEndpoint", ['path', 'timeout'])

LOGGER = logging.getLogger(__name__)


def get_api_error_details(response):
    try:
        b = response.json()
    except ValueError:
        b = str(response.content[:256])

    return {
        'url': response.request.url,
        'request.body': str(response.request.body),
        'response.body': b,
    }


class APIError(Exception):
    def __init__(self, *args, exc_info=None, cls=None, endpoint=None):
        """
        Args:
            *args:
            exc_info (requests.RequestException):
        """
        self.exc = exc_info
        klass = (cls or '').replace('_', '').replace('Client', '')
        if endpoint and klass:
            msg = self.get_message(exc_info, endpoint, klass)
            if isinstance(self.exc, requests.HTTPError) and exc_info.response is not None:
                LOGGER.error(
                    "API Error: status=%s, details=%s",
                    exc_info.response.status_code,
                    json.dumps(get_api_error_details(exc_info.response)),
                )
            super().__init__(msg, *args)
        else:
            super().__init__(*args)

    @staticmethod
    def get_formatted_error(response):
        try:
            raw = response.json()
            error = raw.get('error') or raw.get('errors')

            if isinstance(error, list):
                error = error[0]

            if isinstance(error, str):
                return error

            if isinstance(error, dict):
                return '%s (%s)' % (error.get('name'), error.get('message'))

            return error
        except (AttributeError, ValueError):
            return

    @classmethod
    def get_message(cls, exc, endpoint, klass):
        if isinstance(exc, requests.Timeout):
            return '%s @ %s (%s)' % (
                exc.__class__.__name__,
                endpoint.path,
                klass,
            )
        elif isinstance(exc, requests.ConnectionError):
            return 'Error connecting to %s' % (klass,)
        elif isinstance(exc, requests.HTTPError):
            fmt = cls.get_formatted_error(exc.response)
            return "%s @ %s (%s)" % (
                fmt or exc.response.reason,
                endpoint.path,
                klass,
            )
        else:
            return '%s in API call to %s (%s)' % (
                exc.__class__.__name__,
                endpoint.path,
                klass,
            )

    def get_status_code(self):
        if hasattr(self.exc, 'response') and hasattr(self.exc.response, 'status_code'):
            return self.exc.response.status_code
        return None

    def get_response_json(self):
        try:
            if hasattr(self.exc, 'response'):
                return self.exc.response.json()
            return {}
        except ValueError:
            return {}


class APISession(requests.Session):
    def __init__(self, base_url, headers=None, name=None):
        super().__init__()
        self._base_url = base_url
        self._name = name
        self.headers.update({'User-Agent': 'payments'})
        if isinstance(headers, dict):
            self.headers.update(headers)

    def requests_retry_session(self,
                               retries=3,
                               backoff_factor=0.3,
                               status_forcelist=(500, 502, 504)):
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.mount('http://', adapter)
        self.mount('https://', adapter)
        return self

    def request(self, method, endpoint, path_kwargs=None, **kwargs):
        """
        Args:
            method (str):
            endpoint (APIEndpoint):
            path_kwargs (dict): List of values that will be interpolated in the URL
             (using endpoint.format(**path_kwargs)).
        """
        if path_kwargs is not None:
            url = self._base_url + endpoint.path.format(**path_kwargs)
        else:
            url = self._base_url + endpoint.path
        kwargs.setdefault('timeout', endpoint.timeout)

        try:
            resp = super().request(method, url, **kwargs)
            resp.raise_for_status()
            return resp
        except requests.HTTPError as e:
            if e.response.status_code >= 500:
                LOGGER.error((e.response.content or '')[:1000])
            LOGGER.exception(e)
            raise APIError(exc_info=e, cls=self._name, endpoint=endpoint)
        except requests.ConnectionError as e:
            raise APIError(exc_info=e, cls=self._name, endpoint=endpoint)
        except requests.Timeout as e:
            raise APIError(exc_info=e, cls=self._name, endpoint=endpoint)
        except requests.RequestException as e:
            raise APIError(exc_info=e, cls=self._name, endpoint=endpoint)


class APIClient:
    base_url = None
    headers = None

    def get_base_url(self):
        return self.base_url

    def get_headers(self):
        return self.headers

    def __init__(self):
        assert self.base_url is not None, (
            'Class {} missing "base_url" attribute'.format(self.__class__.__name__)
        )
        self.session = APISession(
            self.get_base_url(),
            headers=self.get_headers(),
            name=self.__class__.__name__,
        )
