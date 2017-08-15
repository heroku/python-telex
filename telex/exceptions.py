class RequestException(IOError):
    def __init__(self, *args, **kwargs):
        self.requests_exc = kwargs.pop('requests_exc', None)
        self.response = kwargs.pop('response', None)
        super(RequestException, self).__init__(*args, **kwargs)
