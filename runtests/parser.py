from pynoveldoc.compiler import parse
from pynoveldoc.serialize import to_dict, from_dict
from prettyprinter import pprint, install_extras

install_extras(exclude=["django", "ipython"])

got = parse(
    filename=__file__,
    text=r"""
Story Start

SET lfkdsk = 100  
SET v = script(1, "lfkdsk")

SAY 「lfkdsklfkdskfuck 」

# comment test

A SAY 「dsk」
A [Angry] SAY 「dsk」

START STORY novel1
END novel1

> BGMStop
> BGM Eff.music 

Choice :
「1.」  -> novel1
「2.」  -> novel2
「3.」  -> novel3

- []
+ []
+ [ A ]
+ [ A, B, C ]

[] -> Hello
[ A ] -> Hello 
[ 好感度 ] -> 上升

===== Chapter One =====

Story End

""",
)

# pprint(got)

pprint(from_dict(to_dict(got)))

