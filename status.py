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


# The class name violates PEP8, but that's okay. I like `status.HTTP_200_OK`
# compared to `status.HTTP_200_OK` and `status` is not used as class in strict
# sense and neither it requires to create `status` objects.
class status(object):

    HTTP_100_CONTINUE = 100
    HTTP_101_SWITCHING_PROTOCOLS = 101
    HTTP_200_OK = 200
    HTTP_201_CREATED = 201
    HTTP_202_ACCEPTED = 202
    HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
    HTTP_204_NO_CONTENT = 204
    HTTP_205_RESET_CONTENT = 205
    HTTP_206_PARTIAL_CONTENT = 206
    HTTP_300_MULTIPLE_CHOICES = 300
    HTTP_301_MOVED_PERMANENTLY = 301
    HTTP_302_FOUND = 302
    HTTP_303_SEE_OTHER = 303
    HTTP_304_NOT_MODIFIED = 304
    HTTP_305_USE_PROXY = 305
    HTTP_306_RESERVED = 306
    HTTP_307_TEMPORARY_REDIRECT = 307
    HTTP_308_RESUME_INCOMPLETE = 308
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_402_PAYMENT_REQUIRED = 402
    HTTP_403_FORBIDDEN = 403
    HTTP_404_NOT_FOUND = 404
    HTTP_405_METHOD_NOT_ALLOWED = 405
    HTTP_406_NOT_ACCEPTABLE = 406
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
    HTTP_408_REQUEST_TIMEOUT = 408
    HTTP_409_CONFLICT = 409
    HTTP_410_GONE = 410
    HTTP_411_LENGTH_REQUIRED = 411
    HTTP_412_PRECONDITION_FAILED = 412
    HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
    HTTP_414_REQUEST_URI_TOO_LONG = 414
    HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
    HTTP_417_EXPECTATION_FAILED = 417
    HTTP_418_I_AM_A_TEAPOT = 418
    HTTP_422_UNPROCESSABLE_ENTITY = 422
    HTTP_428_PRECONDITION_REQUIRED = 428
    HTTP_429_TOO_MANY_REQUESTS = 429
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    HTTP_500_INTERNAL_SERVER_ERROR = 500
    HTTP_501_NOT_IMPLEMENTED = 501
    HTTP_502_BAD_GATEWAY = 502
    HTTP_503_SERVICE_UNAVAILABLE = 503
    HTTP_504_GATEWAY_TIMEOUT = 504
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511

    @staticmethod
    def is_informational(code):
        return 100 <= code <= 199

    @staticmethod
    def is_success(code):
        return 200 <= code <= 299

    @staticmethod
    def is_redirect(code):
        return 300 <= code <= 399

    @staticmethod
    def is_client_error(code):
        return 400 <= code <= 499

    @staticmethod
    def is_server_error(code):
        return 500 <= code <= 599

    @staticmethod
    def describe(code):
        status_codes = {v: k for k, v in get_dict_iterable(status.__dict__)
                        if k.startswith('HTTP_')}
        try:
            return status_codes[code]
        except KeyError:
            raise InvalidHTTPStatusCode


# Some helper things

# I should use `six` here, probably. but then `distutils` doesn't support
# `install_requires`
def get_dict_iterable(dictionary):
    if sys.version_info[0] == 2:
        return dictionary.iteritems()
    else:
        return dictionary.items()
