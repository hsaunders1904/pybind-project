from . import _cpplib


def hello() -> str:
    return _cpplib.hello()
