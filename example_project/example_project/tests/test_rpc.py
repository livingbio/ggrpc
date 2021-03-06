import json

import mock
from django.test import Client
from django.urls import reverse

from ggrpc.utils import client_factory
from ..views import FakeService


client = Client()


def _fake_call(name, *args, **kwargs):
    response = client.post(reverse("rpc", args=(name, )), {
        "params": json.dumps({
            "args": args,
            "kwargs": kwargs
        }),
    })

    assert response.status_code == 200
    return json.loads(response.content)


@mock.patch('ggrpc.rpc_client.RPCClient._call', side_effect=_fake_call)
def test_create_service(mock_func):
    code = client_factory(FakeService)

    exec(code)
    service = FakeService("http://a.fake.url/")

    assert service.add(1, 2) == 3
    assert service.my_sum(1, 2, 3) == 6
