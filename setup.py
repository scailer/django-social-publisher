# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys

from setuptools import setup, find_packages

DESCRIPTION = """
Extension for python-social-auth [https://pypi.python.org/pypi/python-social-auth/]
that add ability to create posts in social nets from registered user directly.

Module contains pluggable system of social-nets backends and handlers for adapt
user content to social nets API format.

For writing you own haandlers, see examples in source code.
"""


REQUIREMENTS = {
    "py3": {
        "facebook": ["requests-facebook-py3"],
        "tumblr": ["Py3Tumblr"],
        "vk": ["vk==1.5.3"],
        "twitter": ["twython==3.2.0"],
        "ok": ["odnoklassniki"]
    },
    "py2": {
        "facebook": ["requests-facebook==0.2.0"],
        "tumblr": ["PyTumblr==0.0.6"],
        "vk": ["vk==1.5.3"],
        "twitter": ["twython==3.2.0"],
        "ok": ["odnoklassniki"]
    }
}

DEPENDENCY_LINKS = [
    "https://github.com/michaelhelmick/requests-facebook.git",
    "https://github.com/scailer/pytumblr.git@diana/python-3-support",
]

PY3 = sys.version_info[0] == 3

setup(
    name='django-social-publisher',
    version='0.5.6',
    author='Dmitriy Vlasov',
    author_email='scailer@veles.biz',

    include_package_data=True,
    packages=find_packages(),

    url='https://github.com/scailer/django-social-publisher/',
    license='MIT license',
    description='Server-side content publishing extension for django-social-auth.',
    long_description=DESCRIPTION,

    install_requires=[
        'python-social-auth==0.2.14'
    ],

    classifiers=(
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),

    dependency_links=DEPENDENCY_LINKS,
    extras_require=REQUIREMENTS.get(PY3 and 'py3' or 'py2'),
)
