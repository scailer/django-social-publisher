# -*- coding: utf-8 -*-

from setuptools import setup
import sys
reload(sys).setdefaultencoding("UTF-8")

setup(
    name='django-social-publisher',
    version='0.1a',
    author='Dmitriy Vlasov',
    author_email='scailer@russia.ru',

    include_package_data=True,
    packages=[
        'social_publisher',
        'social_publisher.backends',
        'social_publisher.handlers'
    ],

    url='https://github.com/scailer/django-social-publisher/',
    license='MIT license',
    description=(u'Server-side content publishing extantion for '
                 u'django-social-auth.').encode('utf8'),
    long_description=(
        u'Add ability to create content in social nets from '
        u'users attached with django-social-auth.'
    ).encode('utf8'),

    install_requires=[
        'django-social-auth>=0.7'
    ],

    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: Russian',
    ),
)
