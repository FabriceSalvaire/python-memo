#r# ============================
#r#  Annotations and Type Hints
#r# ============================
#r#
#r# This page contains a memo on annotations.
#r#
#r# * https://docs.python.org/3/library/typing.html#module-typing
#r# * `PEP 484 – Type Hints <https://www.python.org/dev/peps/pep-0484>`_
#r# * `PEP 483 – The Theory of Type Hints <https://www.python.org/dev/peps/pep-0483>`_
#r#
#r# Static type checker for Python:
#r#
#r# * `Mypy <http://mypy-lang.org>`_  a static type checker for Python
#r# * `PyAnnotate <https://github.com/dropbox/pyannotate>`_
#r#

#r# Let a function with an a required parameter and a default one:

def greeting(name, prefix='Mr.'):
   return 'Hello, {} {}'.format(name, prefix)

#r# Same function with annotations:

def greeting(name: str, prefix: str = 'Mr.') -> str:
   return 'Hello, {} {}'.format(name, prefix)

print(greeting.__annotations__)
#o#

#r# A "void" function:

def p() -> None:
    print('hello')

#r# Advanced types:

from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

print(fib.__annotations__)
#o#
