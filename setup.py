#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

# Package meta-data.
NAME = 'pyexample'
DESCRIPTION = 'Example python module'
URL = 'https://github.com/OAustlid/pyexample'
EMAIL = 'OAustlid@gmail.com'
AUTHOR = 'Olve A. Austlid'
REQUIRES_PYTHON = '>=3.8.0'
VERSION = '0.0.1'

# What packages are required for this module to be executed?
REQUIRED = [
    # 'numpy',
]

setup(
    name='pyexample',
    version='0.0.1',
    author='Olve A. Austlid',
    author_email="OAustlid@gmail.com",
    packages=['pyexample'],
    scripts=[],
    license='LICENSE',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=[],
)