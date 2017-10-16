
from django.http import HttpResponse
from django.views import View

from .utils import get_coder


class RPCView(View):
    # TODO: Support other framework
    # TODO: add async / batch mode

    def post(self, request, method):
        # A simple RPC implementation, may switch to gRPC in the future
        method = getattr(self, method)

        format = request.POST.get('format', 'json')
        coder = get_coder(format)

        params = coder.loads(request.POST.get('params'))
        result = method(*params['args'], **params['kwargs'])

        return HttpResponse(coder.dumps(result))
