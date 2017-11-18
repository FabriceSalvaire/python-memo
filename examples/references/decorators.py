#!# ============
#!#  Decorators
#!# ============
#!#
#!# This page contains a memo on decorators.

####################################################################################################

from Tools import *

####################################################################################################
#!#
#!# Function Decorators
#!# -------------------
#!#
#!# `PEP 318 -- Class Decorators <https://www.python.org/dev/peps/pep-318>`_

def func_decorator_1(func):
    print_function('func_decorator_1', func)
    # do something with func
    # func.attribute = ...
    return func

def func_decorator_2(func):
    print_function('func_decorator_2', func)
    return func

# Same as foo = func_decorator_2(func_decorator_1(foo))
@func_decorator_2
@func_decorator_1
def foo():
  pass

#o#

class func_decorator_3:

    def __init__(self, *args, **kwargs):
        print_method(self, '__init__', args, kwargs)

    def __call__(self, func):
        print_method(self, '__call__', func)
        return func

# Same as foo = func_decorator_3(*args, **kwargs)(foo)
@func_decorator_3(1, 2, attr1='abc')
def foo():
  pass

#o#

####################################################################################################
#!#
#!# Class Decorators
#!# ----------------
#!#
#!# `PEP 3129 -- Class Decorators <https://www.python.org/dev/peps/pep-3129>`_

def class_decorator_1(cls):
    print_function('class_decorator_1', cls)
    # cls.attribute = ...
    return cls

def class_decorator_2(cls):
    print_function('class_decorator_2', cls)
    return cls

# Same as A = class_decorator_2(class_decorator_1(A))
@class_decorator_2
@class_decorator_1
class A:
  pass

#o#
