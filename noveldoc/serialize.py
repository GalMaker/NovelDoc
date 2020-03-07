from collections import defaultdict


dispatch_to_dict = defaultdict(dict)
dispatch_from_dict = defaultdict(dict)


def _as_is(x):
    return x


def _support(cls):
    dispatch_to_dict[cls.__module__][cls.__name__] = _as_is


_support(int)
_support(float)
_support(complex)
_support(str)
_support(bool)
_support(None.__class__)


def _list_support(x):
    return [to_dict(e) for e in x]

dispatch_to_dict[list.__module__][list.__name__] = _list_support
dispatch_to_dict[tuple.__module__][tuple.__name__] = _list_support


def to_dict(o, dispatch_to_dict=dispatch_to_dict):
    cls = o.__class__
    mod = cls.__module__
    name = cls.__name__
    data = dispatch_to_dict[mod][name](o)
    return data


def from_dict(data, dispatch_from_dict=dispatch_from_dict):
    if isinstance(data, dict):
        cls = data.get("__class__")
        if cls is not None:
            cls_mod, cls_name = cls
            return dispatch_from_dict[cls_mod][cls_name](data)
    elif isinstance(data, (list, tuple)):
        return list(map(from_dict, data))
    return data


def dict_support(cls):
    try:
        o_fields = tuple(cls.__annotations__)
    except AttributeError:
        o_fields = ()

    def to_dict_impl(
        o, fields=o_fields, to_dict=to_dict, mod=cls.__module__, name=cls.__name__,
    ):
        data = {field: to_dict(getattr(o, field)) for field in fields}
        data["__class__"] = (mod, name)
        return data

    def from_dict_impl(data, fields=o_fields, cls=cls, from_dict=from_dict):
        o = object.__new__(cls)
        for field in fields:
            setattr(o, field, from_dict(data[field]))

        return o

    dispatch_from_dict[cls.__module__][cls.__name__] = from_dict_impl
    dispatch_to_dict[cls.__module__][cls.__name__] = to_dict_impl
    return cls

