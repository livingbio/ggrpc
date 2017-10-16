
import requests

from .utils import get_coder


class RPCClient(object):
    def __init__(self, base_uri, format='json'):
        assert base_uri.endswith('/'), "{} needs endswith /".format(base_uri)

        self.base_uri = base_uri
        self.format = format
        self.coder = get_coder(format)

    def _call(self, method, *args, **kwargs):
        response = requests.post(self.base_uri + method, {
            "format": format,
            "params": self.coder.dumps({
                "args": args,
                "kwargs": kwargs
            })
        })

        return self.coder.loads(response.content)
