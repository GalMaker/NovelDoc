from rbnf_rts.routine import DQString
from rbnf_rts.rts import Tokens, State
from pynoveldoc import docast
from pynoveldoc.grammar import run_lexer, mk_parser

ctx = {'Str': DQString}
co = mk_parser.__code__
requires = co.co_varnames[:co.co_argcount]

for each in requires:
    if each not in ctx:
        ctx[each] = getattr(docast, each)

parse = mk_parser(**ctx)

tokens = list(run_lexer("<current file>", """
NOVEL_START
SET lfkdsk = 100  
SET v = "lfkdsk"

SAY "lfkdsk
lfkdsk
fuck
"

SAY A "dsk"

START novel1 STORY
END novel1

NOVEL_END
"""))
print(tokens)
got = parse(State(), Tokens(tokens))
print(got)
