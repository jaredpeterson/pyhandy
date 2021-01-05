#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyHandy is a simple Python library for handling basic IO operations.
"""

import setuptools

import pyhandy

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='pyhandy',
    version=pyhandy.__version__,
    description='PyHandy is a simple Python library for handling basic IO operations.',
    long_description=long_description,
    author=pyhandy.__author__,
    author_email=pyhandy.__email__,
    packages=['pyhandy'],
    install_requires=['pytest>=6.2.1', 'pandas >= 1.0.3']
)
