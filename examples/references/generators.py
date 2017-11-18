#!# ============
#!#  Generators
#!# ============
#!#
#!# This page contains a memo on generators.
#!#
#!# For a complete reference documentation, look at
#!# https://docs.python.org/3/reference/expressions.html#generator-expressions

####################################################################################################

from Tools import *

import asyncio

####################################################################################################

#!# List Comprehensions
#!# -------------------

a_list = [x for x in range(10)]
print(a_list)
#o#

a_set = {x % 10 for x in range(100)}
print(a_set)
#o#

a_dict = {x:x for x in range(5)}
print(a_dict)
#o#

#!# Nested List Comprehensions
#!# ~~~~~~~~~~~~~~~~~~~~~~~~~~

a_list_of_list = [[x, y]
                  for x in range(2)
                  for y in range(4)]
print(a_list_of_list)
#o#

#!# Filtered List Comprehensions
#!# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a_list = [x for x in range(10)
          if 2 <= x <= 6]
print(a_list)
#o#

a_list_of_list = [[x, y]
                  for x in range(10)
                  for y in range(10)
                  if 2 <= x <= 3 and 5 <= y <= 6]
print(a_list_of_list)
#o#

####################################################################################################

#!# Generator expressions
#!# ---------------------

N = 4
multiplication_table = (x*y for x in range(1, N+1) for y in range(1, N+1))

print(list(multiplication_table))
#o#

#!# Yield expressions
#!# -----------------

def simplist_generator():
    yield 1

print(list(simplist_generator()))
#o#

def range_clone(N):
    for i in range(N):
        yield i

print(list(range_clone(10)))
#o#

#!# A generator exit when :code:`StopIteration` is raised:

def generator(N, M):
    value = N
    while True:
        yield value
        value += 1
        if M <= value:
            raise StopIteration

print(list(generator(10, 20)))
#o#

#!# We can yield from a generator instead of a value:

def generator(N):
    yield from range_clone(N)

print(list(generator(10)))
#o#

#!# Generator-iterator Methods
#!# --------------------------

def echo(value=None):
    print("echo is running")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as exception:
                print('exception:', exception)
                value = exception
    finally:
        # cleanup code
        print("reached finally")

generator = echo(1)
#o#

#!# Starts the execution of a generator function or resumes it at the last executed yield expression.

print(next(generator))
#o#

print(next(generator))
#o#

#!# Resumes the execution and “sends” a value into the generator function.

print(generator.send(2))
#o#

#!# Raises an exception of type type at the point where the generator was paused.

# generator.throw(type[, value[, traceback]])
generator.throw(TypeError, "spam")
#o#

#!# Raises a :code:`GeneratorExit` at the point where the generator function was paused.

generator.close()
#o#

#!# Asynchronous Generator Functions
#!# --------------------------------

#!# **To be completed**
#!#
#!# For further information see `PEP 525 -- Asynchronous Generators <https://www.python.org/dev/peps/pep-0525>`_

async def ticker(delay, to):
    """Yield numbers from 0 to `to` every `delay` seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

#!# Asynchronous Generator-Iterator Methods
#!# ---------------------------------------

#!# **To be completed**
