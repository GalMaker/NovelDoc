import sys
from importlib import import_module
import_module('runtests.{}'.format(sys.argv[1]))
