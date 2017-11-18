#!# =======
#!#  Scope
#!# =======
#!#
#!# This page contains a memo on scope.

####################################################################################################

from Tools import *

####################################################################################################

#!# Upper scope
#!# -----------

#!# Attributes are local to the "__main__" Python file or a module

a_global = 1 # in fact local to upper scope
print(a_global)
#o#

#!# _ prefixed attributes are privates by convention
_a_private_global = 2

#!# Module Scope
#!# ~~~~~~~~~~~~

#?# Fixme: #i# don't work

#!# Let a module :file:`ModuleA/__init__.py`

#itxt# ModuleA/__init__.py

import ModuleA
#o#

#!# Loops
#!# ~~~~~

for i in range(10):
    # i is local to the upper scope
    pass

print('i' in globals())
print('last i is', i)
#o#

#!# With statement
#!# ~~~~~~~~~~~~~~

with open(__file__) as fh:
    # fh is local to the upper scope
    print(type(fh))
print(type(fh))
#o#

#!# Test for main
#!# -------------

if __name__ == '__main__':
    print('This file is main')

#!# Function scope
#!# --------------

another_global = 1

def foo():
    tmp_local = 1 # temporary attribute in function scope
    another_global = 2 # idem
    # global id1, id2, ...
    global a_global # use attribute defined at top level (global)
    print_function('foo', a_global, another_global)

try:
    print(tmp_local)
except NameError as exception:
    print(exception)

foo()
#o#

def outside():
    tmp_local = "outside"
    def inside():
        tmp_local = "inside"
        print_function('inside', tmp_local)
    inside()
    print_function('outside', tmp_local)

outside()
#o#

def outside():
    tmp_local = "outside"
    def inside():
        # nonlocal id1, id2, ...
        nonlocal tmp_local # # use attribute defined at upper level
        tmp_local = "inside"
        print_function('inside', tmp_local)
    inside()
    print_function('outside', tmp_local)

outside()
#o#

#!# We can attach attributes to function

foo.attribute = 1

#!# Class scope
#!# -----------

class Foo:

    # We can execute codes in class declaration !
    print('building Foo')

    attribute = 1 # local attribute in class scope

    # _ prefixed attributes are privates by convention
    _private_attribute = 2

    # __ prefixed attributes are prefixed by class name
    # "__foo_attribute" is mangled to "Foo__foo_attribute"
    __foo_attribute = 3

    def __init__(self):
        print_method(self, '__init__')

    # This method cannot be overridden in subclasses
    def __method(self):
        print_method('Foo', '__method', self)

    def method(self):
        print_method(self, 'method')
        self.__method() # call Foo__foo_attribute

#!# We can complete class later

Foo.attribute = 2

def another_method(self):
    print_method(self, 'another_method')
Foo.another_method = another_method
#o#

obj = Foo()
obj.method()
obj.another_method()
#o#

class Bar(Foo):

    def __method(self):
        print_method('Bar', '__method', self)

obj = Bar()
obj.method()
#o#
