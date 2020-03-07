from __future__ import annotations
from dataclasses import dataclass
from noveldoc.serialize import to_dict, from_dict, dict_support


@dict_support
@dataclass
class X:
    x: object
    s: object

    def __init__(self, x, s):
        self.x = x
        self.s = s


@dict_support
@dataclass
class S:
    x: object
    y: list

    def __init__(self, x, y):
        self.x = x
        self.y = y


data = to_dict(X(1.0, S(2.0, [S(1.0, [])])))
print(data)

print(from_dict(data))


data = to_dict(X("xxxx", S(S(1.0, [X("xxx", "xx")]), [])))
print(data)

print(from_dict(data))

