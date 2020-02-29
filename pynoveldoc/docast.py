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
class SayWhat:
    loc: Location
    sm: str
    say: str
    status: t.List[Status]


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
    lines: t.List[Stmt]


@dataclass
class ChoiceItem:
    loc: Location
    choice_text: str
    point_to: str


@dataclass
class Status:
    loc: Location
    status: str
    action: str


@dataclass
class Choice:
    loc: Location
    choices: t.List[ChoiceItem]


Stmt = t.Union[Let, Label, SayWhat, Doc, Command, Choice]
Expr = t.Union[List, Lit, Status]
