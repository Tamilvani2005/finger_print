# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. This API can be used for data exports, decision-making, and data analysis scenarios.  # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import unittest

import urllib3

from fingerprint_pro_server_api_sdk import Configuration, ManyRequestsResponse, ErrorVisits403, ErrorEvent403Response, \
    ErrorEvent404Response
from fingerprint_pro_server_api_sdk.api.fingerprint_api import FingerprintApi  # noqa: E501
from fingerprint_pro_server_api_sdk.rest import KnownApiException

API_KEY = 'private_key'

VERSION = '4.1.0.dev1'


class MockPoolManager(object):
    def __init__(self, tc):
        self._tc = tc
        self._reqs = []

    def expect_request(self, *args, **kwargs):
        self._reqs.append((args, kwargs))

    @staticmethod
    def get_mock_from_path(path):
        return path.split('/')[-1]

    def request(self, *args, **kwargs):
        self._tc.assertTrue(len(self._reqs) > 0)
        r = self._reqs.pop(0)
        status = 200
        if r[1].get('status') is not None:
            status = r[1].get('status')
            r[1].pop('status')
        self._tc.maxDiff = None
        self._tc.assertEqual(r[0], args)
        self._tc.assertEqual(r[1], kwargs)

        # TODO Add support for more complex paths?
        mock_file_by_visitor_id = MockPoolManager.get_mock_from_path(r[0][1])

        if mock_file_by_visitor_id == 'bad_text_data':
            return urllib3.HTTPResponse(status=200, body='really bad data')
        if mock_file_by_visitor_id == 'bad_json_data':
            return urllib3.HTTPResponse(status=200, body='{}')
        try:
            with io.open('./test/mocks/' + mock_file_by_visitor_id, 'r', encoding='utf-8') as mock_file:
                answer_mock = mock_file.read()
                mock_file.close()
            headers = {}
            if mock_file_by_visitor_id == 'visits_too_many_requests_error.json':
                headers.update({'Retry-After': '4'})

            return urllib3.HTTPResponse(status=status, body=answer_mock, headers=headers)
        except IOError as e:
            print(e)
            return urllib3.HTTPResponse(status=200, body='{"visitorId": "%s", "visits": []}' % mock_file_by_visitor_id)
            pass


class TestFingerprintApi(unittest.TestCase):
    """FingerprintApi unit test stubs"""

    def setUp(self):
        configuration = Configuration(api_key=API_KEY, region="us")
        self.api = FingerprintApi(configuration)  # noqa: E501
        self.integration_info = ('ii', 'fingerprint-pro-server-python-sdk/%s' % VERSION)
        self.request_headers = {
            'Content-Type': 'application/json',
            'Auth-API-Key': 'private_key',
            'Accept': 'application/json',
            'User-Agent': 'Swagger-Codegen/%s/python' % VERSION
        }

    def tearDown(self):
        pass

    @staticmethod
    def get_get_visits_method_path(visitor_id, region='us'):
        domain = {
            "us": "api.fpjs.io",
            "eu": "eu.api.fpjs.io",
            "ap": "ap.api.fpjs.io",
        }.get(region, "api.fpjs.io")
        return 'https://%s/visitors/%s' % (domain, visitor_id)

    @staticmethod
    def get_get_event_method_path(request_id, region='us'):
        domain = {
            "us": "api.fpjs.io",
            "eu": "eu.api.fpjs.io",
            "ap": "ap.api.fpjs.io",
        }.get(region, "api.fpjs.io")
        return 'https://%s/events/%s' % (domain, request_id)

    def test_get_visits_correct_data(self):
        """Test checks correct code run result in default scenario"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file1 = 'visits_limit_1.json'
        mock_file2 = 'visits_limit_500.json'
        mock_file3 = 'visits_limit_500.json'
        mock_file4 = 'visits_limit_500.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file1),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file2),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file3),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file4),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        self.api.get_visits(mock_file1)
        self.api.get_visits(mock_file2)

    def test_get_visits_error_403(self):
        """Test checks correct code run result in case of 403 error"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file = 'visits_403_error.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None, status=403)
        with self.assertRaises(KnownApiException) as context:
            self.api.get_visits(mock_file)
        self.assertEqual(context.exception.status, 403)
        structured_error = context.exception.structured_error
        self.assertIsInstance(context.exception.structured_error, ErrorVisits403)

    def test_get_visits_error_429(self):
        """Test checks correct code run result in case of 429 error"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file = 'visits_too_many_requests_error.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None, status=429)
        with self.assertRaises(KnownApiException) as context:
            self.api.get_visits(mock_file)
        self.assertEqual(context.exception.status, 429)
        self.assertIsInstance(context.exception.structured_error, ManyRequestsResponse)
        self.assertEqual(context.exception.structured_error.retry_after, 4)

    def test_get_visits_error_429_empty_retry_after(self):
        """Test checks correct code run result in case of 429 error"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file = 'visits_too_many_requests_error_empty_header.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mock_file),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None, status=429)
        with self.assertRaises(KnownApiException) as context:
            self.api.get_visits(mock_file)
        self.assertEqual(context.exception.status, 429)
        self.assertIsInstance(context.exception.structured_error, ManyRequestsResponse)
        self.assertEqual(context.exception.structured_error.retry_after, 1)

    def test_get_event_correct_data(self):
        """Test checks correct code run result in default scenario"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file1 = 'get_event.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mock_file1),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)

        self.api.get_event(mock_file1)

    def test_get_event_errors_200(self):
        """Test checks correct code run result in scenario of arrors in BotD or identification API"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file_botd_fail = 'get_event_botd_failed_error.json'
        mock_file_botd_429 = 'get_event_botd_too_many_requests_error.json'
        mock_file_identification_fail = 'get_event_identification_failed_error.json'
        mock_file_identification_429 = 'get_event_identification_too_many_requests_error.json'
        mock_file_all_errors = 'get_event_all_errors.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mock_file_botd_fail),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mock_file_botd_429),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET',
                                 TestFingerprintApi.get_get_event_method_path(request_id=mock_file_identification_fail),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET',
                                 TestFingerprintApi.get_get_event_method_path(request_id=mock_file_identification_429),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mock_file_all_errors),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)

        self.api.get_event(mock_file_botd_fail)
        self.api.get_event(mock_file_botd_429)
        self.api.get_event(mock_file_identification_fail)
        self.api.get_event(mock_file_identification_429)
        self.api.get_event(mock_file_all_errors)

    def test_get_event_error_403(self):
        """Test checks correct code run result in case of 403 error"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file = 'get_event_403_error.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mock_file),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None, status=403)
        with self.assertRaises(KnownApiException) as context:
            self.api.get_event(mock_file)
        self.assertEqual(context.exception.status, 403)
        self.assertIsInstance(context.exception.structured_error, ErrorEvent403Response)

    def test_get_event_error_404(self):
        """Test checks correct code run result in case of 403 error"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mock_file = 'get_event_404_error.json'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mock_file),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None, status=404)
        with self.assertRaises(KnownApiException) as context:
            self.api.get_event(mock_file)
        self.assertEqual(context.exception.status, 404)
        self.assertIsInstance(context.exception.structured_error, ErrorEvent404Response)

    def test_get_event_empty_data(self):
        """Test checks correct code running in case of there is no events"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'empty_answer'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_event_method_path(request_id=mocked_id),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)

        response = self.api.get_event(mocked_id)
        self.assertEqual(response.products, None)

    def test_get_visits_empty_answer(self):
        """Test checks correct code running in case of there is no visits"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'empty_answer'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mocked_id),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        self.assertEqual(self.api.get_visits(mocked_id).visits, [])

    def test_get_visits_bad_text_data(self):
        """Test checks exception raising when client receives not a JSON answer"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'bad_text_data'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mocked_id),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        with self.assertRaises(ValueError):
            self.api.get_visits(mocked_id)

    def test_get_visits_bad_json_data(self):
        """Test checks exception raising when client receives a bad JSON answer"""
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'bad_json_data'
        mock_pool.expect_request('GET', TestFingerprintApi.get_get_visits_method_path(visitor_id=mocked_id),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        with self.assertRaises(ValueError):
            self.api.get_visits(mocked_id)

    def test_init_with_us_region(self):
        """Test that link for us region generates correct"""
        configuration = Configuration(api_key=API_KEY, region="us")
        self.api = FingerprintApi(configuration)  # noqa: E501
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'empty_answer'
        mock_pool.expect_request('GET',
                                 TestFingerprintApi.get_get_visits_method_path(visitor_id=mocked_id, region="us"),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        self.assertEqual(self.api.get_visits(mocked_id).visits, [])

    def test_init_with_eu_region(self):
        """Test that link for eu region generates correct"""
        configuration = Configuration(api_key=API_KEY, region="eu")
        self.api = FingerprintApi(configuration)  # noqa: E501
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'empty_answer'
        mock_pool.expect_request('GET',
                                 TestFingerprintApi.get_get_visits_method_path(visitor_id=mocked_id, region="eu"),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        self.assertEqual(self.api.get_visits(mocked_id).visits, [])

    def test_init_with_ap_region(self):
        """Test that link for ap region generates correct"""
        configuration = Configuration(api_key=API_KEY, region="ap")
        self.api = FingerprintApi(configuration)  # noqa: E501
        mock_pool = MockPoolManager(self)
        self.api.api_client.rest_client.pool_manager = mock_pool
        mocked_id = 'empty_answer'
        mock_pool.expect_request('GET',
                                 TestFingerprintApi.get_get_visits_method_path(visitor_id=mocked_id, region="ap"),
                                 fields=[self.integration_info], headers=self.request_headers,
                                 preload_content=True, timeout=None)
        self.assertEqual(self.api.get_visits(mocked_id).visits, [])


if __name__ == '__main__':
    unittest.main()
