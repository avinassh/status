#!/usr/bin/env python

from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (ImportError, IOError):
    long_description = open('README.md').read()

version = '1.0.1'

setup(
    name='python-status',
    version=version,
    author='Avinash Sajjanshetty',
    author_email='hi@avi.im',
    py_modules=['status'],
    url='https://github.com/avinassh/status/',
    license='BSD',
    description='HTTP Status for Humans',
    long_description=long_description,
    classifiers=[
        'Development Status :: 6 - Mature',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
