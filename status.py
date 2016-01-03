"""
source: https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/status.py
Copyright (c) 2011-2015, Tom Christie All rights reserved.

Descriptive HTTP status codes, for code readability.

See RFC 2616 - http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
And RFC 6585 - http://tools.ietf.org/html/rfc6585
"""
from __future__ import unicode_literals
import sys


class InvalidHTTPStatusCode(Exception):
    pass


def is_informational(code):
    return 100 <= code <= 199


def is_success(code):
    return 200 <= code <= 299


def is_redirect(code):
    return 300 <= code <= 399


def is_client_error(code):
    return 400 <= code <= 499


def is_server_error(code):
    return 500 <= code <= 599


# Mapping of all human readable text and http status code
_STATUSES = {
    100: 'HTTP_100_CONTINUE',
    101: 'HTTP_101_SWITCHING_PROTOCOLS',
    102: 'HTTP_102_PROCESSING',
    200: 'HTTP_200_OK',
    201: 'HTTP_201_CREATED',
    202: 'HTTP_202_ACCEPTED',
    203: 'HTTP_203_NON_AUTHORITATIVE_INFORMATION',
    204: 'HTTP_204_NO_CONTENT',
    205: 'HTTP_205_RESET_CONTENT',
    206: 'HTTP_206_PARTIAL_CONTENT',
    300: 'HTTP_300_MULTIPLE_CHOICES',
    301: 'HTTP_301_MOVED_PERMANENTLY',
    302: 'HTTP_302_FOUND',
    303: 'HTTP_303_SEE_OTHER',
    304: 'HTTP_304_NOT_MODIFIED',
    305: 'HTTP_305_USE_PROXY',
    306: 'HTTP_306_RESERVED',
    307: 'HTTP_307_TEMPORARY_REDIRECT',
    308: 'HTTP_308_RESUME_INCOMPLETE',
    400: 'HTTP_400_BAD_REQUEST',
    401: 'HTTP_401_UNAUTHORIZED',
    402: 'HTTP_402_PAYMENT_REQUIRED',
    403: 'HTTP_403_FORBIDDEN',
    404: 'HTTP_404_NOT_FOUND',
    405: 'HTTP_405_METHOD_NOT_ALLOWED',
    406: 'HTTP_406_NOT_ACCEPTABLE',
    407: 'HTTP_407_PROXY_AUTHENTICATION_REQUIRED',
    408: 'HTTP_408_REQUEST_TIMEOUT',
    409: 'HTTP_409_CONFLICT',
    410: 'HTTP_410_GONE',
    411: 'HTTP_411_LENGTH_REQUIRED',
    412: 'HTTP_412_PRECONDITION_FAILED',
    413: 'HTTP_413_REQUEST_ENTITY_TOO_LARGE',
    414: 'HTTP_414_REQUEST_URI_TOO_LONG',
    415: 'HTTP_415_UNSUPPORTED_MEDIA_TYPE',
    416: 'HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE',
    417: 'HTTP_417_EXPECTATION_FAILED',
    418: 'HTTP_418_I_AM_A_TEAPOT',
    422: 'HTTP_422_UNPROCESSABLE_ENTITY',
    428: 'HTTP_428_PRECONDITION_REQUIRED',
    429: 'HTTP_429_TOO_MANY_REQUESTS',
    431: 'HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE',
    451: 'HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS',
    500: 'HTTP_500_INTERNAL_SERVER_ERROR',
    501: 'HTTP_501_NOT_IMPLEMENTED',
    502: 'HTTP_502_BAD_GATEWAY',
    503: 'HTTP_503_SERVICE_UNAVAILABLE',
    504: 'HTTP_504_GATEWAY_TIMEOUT',
    505: 'HTTP_505_HTTP_VERSION_NOT_SUPPORTED',
    511: 'HTTP_511_NETWORK_AUTHENTICATION_REQUIRED'
}


def describe(status_code):
    """For a given status code return human readable text.

    :param status_code `int`: HTTP status code.

    >>> describe(200)
    u'HTTP 200 OK'

    >>> describe(-200)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    InvalidHTTPStatusCode: -200 is not a valid status code

    """
    try:
        text = _STATUSES[status_code]
        return text.replace('_', ' ')
    except KeyError:
        raise InvalidHTTPStatusCode(
            u"{} is not a valid status code".format(status_code))


def init():
    """Set required attributes in module
    """
    module = sys.modules[__name__]

    # Make sure status.HTTP_200_OK returns 200
    for status_code, text in _STATUSES.items():
        setattr(module, text, status_code)


init()
