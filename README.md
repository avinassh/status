# status - HTTP Status for Humans

[![version](https://img.shields.io/pypi/v/python-status.svg)](https://pypi.python.org/pypi/python-status/)
[![supported](https://img.shields.io/pypi/pyversions/python-status.svg)](https://pypi.python.org/pypi/python-status/)
![license](https://img.shields.io/pypi/l/python-status.svg)

`status` is a very simple python library which provides human understandable HTTP status codes and improves readability of your code. You don't have to use those ugly HTTP status numbers, but use easily understandable status names.

Don't:

    class PythonPeople(RequestHandler):
        def post(self):
            # do stuff
            return ('That worked!', 201)

But, do this:

    class PythonPeople(RequestHandler):
        def post(self):
            # do stuff
            return ('That worked!', status.HTTP_201_CREATED)


See, that looks so much better. You can use this library wherever you want, from custom python scripts to Django, Flask etc apps. For example, if you were playing with [Requests](http://python-requests.org):

    >>> response = requests.delete('http://some-url')
    >>> response.status_code == status.HTTP_204_NO_CONTENT


## Installation

    pip install python-status


## Usage

`status` comes with HTTP response status codes and also some helpful methods to check the response status. Under the hood, status codes are merely an integer variable with meaningful variable names. Check `status.py` file.

    >>> import status
    >>> status.HTTP_200_OK == 200
    True

For list of available status codes check `status.py` file.

`status` also comes with some helpful methods to check the status of a response. They are `status.is_informational`, `status.is_success`, `status.is_redirect`, `status.is_client_error` and `status.is_server_error`.

    >>> import status
    >>> response = requests.delete('http://some-url')
    >>> if status.is_success(code=response.status_code):
            print('yay!')
    >>> 
    yay!


# Why?

For every project I was creating a `status.py` file in the root directory. So I thought it's better to release this as a package on PyPi and use it.


# License

Please check `LICENSE` for more details.


# Credits

`status` is a fork of [Django Rest Framework](https://github.com/tomchristie/django-rest-framework)(DRF) and is independently maintained. The fork is entirely stripped of all DRF features and is not a submodule of DRF. And it doesn't come with any DRF functionalities.
