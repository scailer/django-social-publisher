# -*- coding: utf-8 -*-

from setuptools import setup

DESCRIPTION = """
Extension for django-social-auth [https://pypi.python.org/pypi/django-social-auth/]
that add ability to create posts in social nets from registered user directly.

Module contains pluggable system of social-nets backends and handlers for adapt
user content to social nets API format.

For writing you own haandlers, see examples in source code.
"""

setup(
    name='django-social-publisher',
    version='0.1.18',
    author='Dmitriy Vlasov',
    author_email='scailer@russia.ru',

    include_package_data=True,
    packages=[
        'social_publisher',
        'social_publisher.backends',
        'social_publisher.handlers',
        'social_publisher.auth'
    ],

    url='https://github.com/scailer/django-social-publisher/',
    license='MIT license',
    description='Server-side content publishing extension for django-social-auth.',
    long_description=DESCRIPTION,

    install_requires=[
        'django-social-auth>=0.7'
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
        'Topic :: Software Development :: Libraries :: Python Modules'
    ),
)
