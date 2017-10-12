from ..rpc_client import client_factory


def create(kls_path, opath=None):
    kls = kls_path.split('.')

    code = client_factory(kls)

    with open(opath, 'w') as ofile:
        ofile.wirte(code)

