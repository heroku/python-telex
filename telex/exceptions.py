# -*- coding: utf-8 -*-


class RequestException(IOError):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.response = kwargs.pop('response', None)
        super(RequestException, self).__init__(*args, **kwargs)
