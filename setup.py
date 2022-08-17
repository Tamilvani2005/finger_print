# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API provides a way for validating visitors’ data issued by Fingerprint Pro.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pathlib
import re

from setuptools import setup, find_packages  # noqa: H301

NAME = "fingerprint-pro-server-api-sdk"
VERSION = "0.0.2"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')
long_description = re.sub("<source[^>]*>\n", '', long_description.replace("<picture>\n", "").replace("</picture>\n", ""))

setup(
    name=NAME,
    version=VERSION,
    description="Fingerprint Pro Server API provides a way for validating visitors’ data issued by Fingerprint Pro.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    license_files=["LICENSE"],
    author="Fingerprint",
    author_email="support@fingerprint.com",
    url="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk",
    keywords=["Swagger", "Fingerprint Pro Server API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security',
    ],
)
