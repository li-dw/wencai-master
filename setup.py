#!/usr/bin/env python
# coding=utf-8
from setuptools import setup




setup(
    name='wencai',
    version='0.1.3',
    author='allen yang',
    author_email='allenyzx@163.com',
    url='https://upload.pypi.org/allenyzx/',
    description='this is a wencai crawler to get message',
    packages=['wencai','wencai/base','wencai/utils'],
    install_requires=[
        "beautifulsoup4",
        "pandas",
        "requests"
    ],
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.5",
    ],
)