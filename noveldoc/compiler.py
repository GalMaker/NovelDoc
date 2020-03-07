from rbnf_rts.routine import DQString
from rbnf_rts.rts import Tokens, State
from noveldoc import docast
from noveldoc.grammar import run_lexer, mk_parser, lexicals

ctx = {'Str': DQString}
co = mk_parser.__code__
requires = co.co_varnames[:co.co_argcount]

for each in requires:
    if each not in ctx:
        ctx[each] = getattr(docast, each)

_parse = mk_parser(**ctx)

def _find_n(s: str, ch, n: int):
    since = 0
    for i in range(0, n - 1):
        since = s.find(ch, since)

    return s[since:s.find(ch, since)]


def case_insensitive(gen):
    ident = lexicals['identifier']
    keywords = {'start', 'end', 'story', 'say', 'set', 'choice'}
    keywords = {k: 'quote {}'.format(k) for k in keywords}
    for each in gen:
        if each.idint is ident:
            value = each.value
            lower = value.lower()
            if value != lower and lower in keywords:
                each.idint = lexicals[keywords[lower]]
        yield each

def parse(text: str, filename: str = "unknown"):
    tokens = list(case_insensitive(run_lexer(filename, text)))

    res = _parse(State(), Tokens(tokens))
    if res[0]:
        return res[1]
    msgs = []
    assert res[1]
    maxline = 0
    for each in res[1]:
        i, msg = each
        token = tokens[i]
        lineno = token.lineno
        maxline = max(lineno, maxline)
        colno = token.colno
        msgs.append(f"Line {lineno + 1}, column {colno}, {msg}")

    e = SyntaxError()
    e.lineno = maxline + 1
    e.msg = '\n'.join(msgs)
    e.filename = filename
    off = token.offset
    e.offset = off
    e.text = text[:text.find('\n', off)]
    raise e
