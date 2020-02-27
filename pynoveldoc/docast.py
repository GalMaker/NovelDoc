from __future__ import annotations

import typing as t
from dataclasses import dataclass

Location = t.Tuple[int, int, str]
DEREF = "!"
WILDCARD = '_'


@dataclass
class Lit:
    loc: Location
    value: object


@dataclass
class Let:
    loc: Location
    name: str
    value: object


@dataclass
class Label:
    loc: Location
    name: str
    is_end: bool


@dataclass
class List:
    loc: Location
    elts: t.List[Expr]


@dataclass
class Say:
    loc: Location
    sm: str
    say: str


@dataclass
class Doc:
    label: Label
    stmts: t.List[Stmt]


@dataclass
class Command:
    loc: Location
    command: str
    args: t.List[Expr]


@dataclass
class Novel:
    stmts: t.List[Stmt]


Stmt = t.Union[Let, Label, Say, Doc, Command]
Expr = t.Union[List, Lit]
