#!# ============================
#!#  Annotations and Type Hints
#!# ============================
#!#
#!# This page contains a memo on annotations.
#!#
#!# * https://docs.python.org/3/library/typing.html#module-typing
#!# * `PEP 484 – Type Hints <https://www.python.org/dev/peps/pep-0484>`_
#!# * `PEP 483 – The Theory of Type Hints <https://www.python.org/dev/peps/pep-0483>`_
#!#
#!# Static type checker for Python:
#!#
#!# * `Mypy <http://mypy-lang.org>`_  a static type checker for Python
#!# * `PyAnnotate <https://github.com/dropbox/pyannotate>`_
#!#

#!# Let a function with an a required parameter and a default one:

def greeting(name, prefix='Mr.'):
   return 'Hello, {} {}'.format(name, prefix)

#!# Same function with annotations:

def greeting(name: str, prefix: str = 'Mr.') -> str:
   return 'Hello, {} {}'.format(name, prefix)

print(greeting.__annotations__)
#o#

#!# A "void" function:

def p() -> None:
    print('hello')

#!# Advanced types:

from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

print(fib.__annotations__)
#o#
