from __future__ import annotations

import typing as t
from dataclasses import dataclass
from pynoveldoc.serialize import dict_support

Location = t.Tuple[int, int, str]
DEREF = "!"
WILDCARD = "_"


@dict_support
@dataclass
class Lit:
    loc: Location
    value: object

@dict_support
@dataclass
class Var:
    loc: Location
    name: str



@dict_support
@dataclass
class Let:
    loc: Location
    name: str
    value: object


@dict_support
@dataclass
class Label:
    loc: Location
    name: str
    is_end: bool


@dict_support
@dataclass
class List:
    loc: Location
    elts: t.List[Expr]


@dict_support
@dataclass
class Call:
    loc: Location
    fn: Expr
    args: t.List[Expr]


@dict_support
@dataclass
class SayWhat:
    loc: Location
    sm: str
    say: str
    status: t.List[Status]


@dict_support
@dataclass
class Doc:
    label: Label
    stmts: t.List[Stmt]


@dict_support
@dataclass
class Command:
    loc: Location
    command: str
    args: t.List[Expr]


@dict_support
@dataclass
class Novel:
    lines: t.List[Stmt]


@dict_support
@dataclass
class ChoiceItem:
    loc: Location
    choice_text: str
    point_to: str


@dict_support
@dataclass
class Status:
    loc: Location
    status: str
    action: str


@dict_support
@dataclass
class Choice:
    loc: Location
    choices: t.List[ChoiceItem]


@dict_support
@dataclass
class Camera:
    loc: Location
    action: str  # bind or unbind
    body: t.Union[List]


@dict_support
@dataclass
class Action:
    loc: Location
    one: str
    action: str


@dict_support
@dataclass
class Chapter:
    loc: Location
    name: t.List[str]


Stmt = t.Union[Let, Label, SayWhat, Doc, Command, Choice, Action, Chapter]
Expr = t.Union[List, Lit, Status, t.List, t.Dict, Var]
