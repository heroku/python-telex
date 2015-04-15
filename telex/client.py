# -*- coding: utf-8 -*-


import json
import requests

from telex import __version__
from telex.exceptions import RequestException


class Client(object):
    def __init__(self, telex_url):
        assert telex_url.startswith('https://'), 'Bad protocol for telex url'

        self.telex_url = telex_url

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'python-telex/{} requests/{}'.format(__version__, requests.__version__)
        })

    def notify_app(self, app_uuid, body, title, action=None):
        return self.post_message('app', app_uuid, body, title, action)

    def notify_user(self, user_uuid, body, title, action=None):
        return self.post_message('user', user_uuid, body, title, action)

    def add_followup(self, message_uuid, body):
        return self._post('/producer/messages/{}'.format(message_uuid), {'body': body})

    def post_message(self, target_type, target_id, title, body, action):
        payload = {
            'title': title,
            'body': body,
            'target': {
                'type': target_type,
                'id': target_id
            }
        }

        if action:
            payload['action'] = action

        return self._post('/producer/messages', payload)

    def _post(self, path, payload):
        try:
            response = self.session.post('{}{}'.format(self.telex_url, path), data=json.dumps(payload))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RequestException(request=e.request, response=e.response)

        return response.json()