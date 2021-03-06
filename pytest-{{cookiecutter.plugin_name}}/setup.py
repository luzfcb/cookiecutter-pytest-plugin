#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-{{cookiecutter.plugin_name}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    maintainer='{{cookiecutter.full_name}}',
    maintainer_email='{{cookiecutter.email}}',
    license='MIT',
    url='https://github.com/{{cookiecutter.github_username}}/pytest-{{cookiecutter.plugin_name}}',
    description='{{cookiecutter.short_description}}',
    long_description=read('README.rst'),
    py_modules=['pytest_{{cookiecutter.plugin_name}}'],
    install_requires=['pytest>={{cookiecutter.pytest_version}}'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            '{{cookiecutter.plugin_name}} = pytest_{{cookiecutter.plugin_name}}',
        ],
    },
)
