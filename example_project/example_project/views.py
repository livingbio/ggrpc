from ggrpc.rpc_server import RPCView


class FakeService(RPCView):
    def add(self, a1, a2):
        return a1 + a2

    def my_sum(self, *args):
        return sum(args)

