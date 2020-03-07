import threading
import os


def watcher():
    rbnf, rlex = '', ''
    while True:
        with open('grammar.exrbnf') as rbnf_f:
            with open('grammar.rlex') as rlex_f:
                new_rbnf = rbnf_f.read()
                new_rlex = rlex_f.read()
                if new_rbnf != rbnf or new_rlex != rlex:
                    os.system(
                        'rbnf-pygen grammar.exrbnf grammar.rlex noveldoc/grammar.py --k 1 --traceback'
                    )
                    rbnf = new_rbnf
                    rlex = new_rlex


if __name__ == '__main__':
    t = threading.Thread(target=watcher)
    t.setDaemon(True)
    t.start()
