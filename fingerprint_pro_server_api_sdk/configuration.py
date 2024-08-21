# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import copy
import logging
import multiprocessing
import sys
import http.client as httplib

from typing import Dict


class Configuration:
    """NOTE: This class is auto generated by the swagger code generator program.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    _default = None

    def __init__(self, api_key: str, region: str = "us"):
        """Constructor"""
        if self._default:
            for key in self._default.__dict__.keys():
                self.__dict__[key] = copy.copy(self._default.__dict__[key])
            return

        # Default Base url
        self.host = self.get_host(region)
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # dict to store API key(s)
        self.api_key = api_key
        # Logging Settings
        self.logger = {"package_logger": logging.getLogger("fingerprint_pro_server_api_sdk"),
                       "urllib3_logger": logging.getLogger("urllib3")}
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

        # Disable client side validation
        self.client_side_validation = True

    @classmethod
    def set_default(cls, default):
        cls._default = default

    @property
    def logger_file(self) -> str:
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :return: The logger_file path.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value: str):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in self.logger.items():
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self) -> bool:
        """Debug status

        :param value: The debug status, True or False.
        """
        return self.__debug

    @debug.setter
    def debug(self, value: bool):
        """Debug status

        :param value: The debug status, True or False.
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in self.logger.items():
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in self.logger.items():
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self) -> str:
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :return: The format string.
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value: str):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def auth_settings(self) -> Dict[str, Dict[str, str]]:
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'ApiKeyHeader':
                {
                    'type': 'api_key',
                    'in': 'header',
                    'key': 'Auth-API-Key',
                    'value': self.api_key
                },
        }

    def get_host(self, region: str) -> str:
        return {
            "us": "https://api.fpjs.io",
            "eu": "https://eu.api.fpjs.io",
            "ap": "https://ap.api.fpjs.io",
        }.get(region, "https://api.fpjs.io")

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 3\n"\
               "SDK Package Version: 7.0.1.dev1".\
               format(env=sys.platform, pyversion=sys.version)
