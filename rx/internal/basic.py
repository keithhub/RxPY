from datetime import datetime
import sys


# Defaults
def noop(*args, **kw):
    """No operation. Returns nothing"""
    pass


def identity(x):
    """Returns argument x"""
    return x


def default_now():
    return datetime.utcnow()


def default_comparer(x, y):
    return x == y


def default_sub_comparer(x, y):
    return x - y


def default_key_serializer(x):
    return str(x)


def default_error(err):
    if isinstance(err, BaseException):
        exc_type, exc_value, exc_tb = sys.exc_info()
        if err == exc_value:
            raise exc_type, exc_value, exc_tb
        raise err
    else:
        raise Exception(err)
