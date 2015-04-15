#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from httmock import urlmatch, response, HTTMock

from telex.client import Client


mock_headers = {'content-type': 'application/json',
               'Set-Cookie': 'foo=bar;'}


@urlmatch(netloc=r'^.*?telex\.mock\.com$', path=r'^/producer/messages$', method='POST')
def message_mock(url, request):
    content = {'success': True}
    return response(200, content, headers=mock_headers, request=request)


@urlmatch(netloc=r'^.*?telex\.mock\.com$', path=r'/producer/messages/[^/]+$', method='POST')
def followup_mock(url, request):
    content = {'success': True}
    return response(200, content, headers=mock_headers, request=request)


class TelexTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client('https://id:key@telex.mock.com')
        self.default_kwargs = {
            'title': 'Welcome to Telex',
            'body': 'Detailed message...',
        }

    def test_notify_app(self):
        self.default_kwargs['app_uuid'] = '123'
        with HTTMock(message_mock):
            r = self.client.notify_app(**self.default_kwargs)
        self.assertTrue(r.get('success'))

    def test_notify_user(self):
        self.default_kwargs['user_uuid'] = '123'
        with HTTMock(message_mock):
            r = self.client.notify_user(**self.default_kwargs)
        self.assertTrue(r.get('success'))

    def test_add_followup(self):
        payload = {'message_uuid': '123', 'body': 'About that invoice...'}
        with HTTMock(followup_mock):
            r = self.client.add_followup(**payload)
        self.assertTrue(r.get('success'))


if __name__ == '__main__':
    unittest.main()