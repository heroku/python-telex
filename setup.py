#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


requires = [
    'requests',
]

version = ''
with open('telex/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

with open('README.md', 'r', 'utf-8') as fd:
    readme = fd.read()


setup(
    name='telex',
    version=version,
    description='Python telex client.',
    long_description=readme,
    license='BSD',
    author='Jeremy West',
    author_email='jeremy@heroku.com',
    url='https://github.com/heroku/python-telex',
    packages=['telex'],
    include_package_data=True,
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)