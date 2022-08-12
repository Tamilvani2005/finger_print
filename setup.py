# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API provides a way for validating visitors’ data issued by Fingerprint Pro.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "fingerprint-pro-server-api-sdk"
VERSION = "0.0.2-beta.4"
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


setup(
    name=NAME,
    version=VERSION,
    description="Fingerprint Pro Server API",
    long_description="file: README.md, CHANGELOG.md, LICENSE",
    license="MIT",
    package_dir="fingerprint_pro_server_api_sdk",
    author_email="support@fingerprint.com",
    url="https://github.com/fingerprintjs/fingerprint-pro-server-api-python-sdk",
    keywords=["Swagger", "Fingerprint Pro Server API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
