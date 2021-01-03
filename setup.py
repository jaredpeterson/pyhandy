#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PyHandy is a simple Python library for handling basic IO operations.
"""

__author__ = 'Jared Peterson'
__license__ = 'apache-2.0'
__maintainer__ = 'Jared Peterson'
__email__ = 'jared.peterson@hey.com'
__version__ = '0.0.1'
__status__ = 'Development'

import setuptools

with open('README.md', 'r') as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name='pyhandy',
    version='0.0.1',
    description='PyHandy is a simple Python library for handling basic IO operations.',
    long_description=long_description,
    author='Jared Peterson',
    author_email='jared.peterson@hey.com',
    packages=['pyhandy'],
    install_requires=['pytest>=6.2.1', 'pandas >= 1.0.3']
)
