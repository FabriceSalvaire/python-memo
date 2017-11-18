#!# ============
#!#  Data model
#!# ============
#!#
#!# This page contains a memo of the Python 3.6 data model.
#!#
#!# For a complete reference documentation, look at https://docs.python.org/3/reference/datamodel.html
#!#

####################################################################################################

import collections
import os

from Tools import *

####################################################################################################
#!#
#!# At __main__ level
#!# -----------------

a_global = 1

print('file:', os.path.basename(__file__))

#o#

####################################################################################################
#!#
#!# Basic Customisation
#!# -------------------

#h# print_rule()

class Foo:

    """Foo is a class"""

    attr1 = 1

    # Arbitrary code
    attr2 = []
    for i in range(10):
        attr2.append(i)

    def __init__(self, *args, **kwargs):
        print_method('Foo', '__init__', self, args, kwargs)

    def method(self, arg1, arg2, attr1='abc'):
        """a method"""

    method.attr1 = 'abc' # set method attributes

    # def __del__(self):
    # def __repr__(self):
    # def __str__(self):
    # def __bytes__(self):
    # def __format__(self, format_spec):

    # def __lt__(self, other):
    # def __le__(self, other):
    # def __eq__(self, other):
    # def __ne__(self, other):
    # def __gt__(self, other):
    # def __ge__(self, other):

    # def __hash__(self):
    # def __bool__(self):

#!#

foo = Foo(1, 2, attr1='abc')
#o#

print(Foo.__class__)
print('doc:', Foo.__doc__)
#o#

pretty_print('dict:', Foo.__dict__)
#o#

print('doc:', Foo.method.__doc__)
print('name:', Foo.method.__name__) # method
print('qualname:', Foo.method.__qualname__) # Foo.method
print('module:', Foo.method.__module__) # __main__
#o#

print('code:', Foo.method.__code__)
print('globals:', Foo.method.__globals__)
#o#

# A tuple containing default argument values for those arguments that have defaults, or None if no
# arguments have a default value
print('defaults:', Foo.method.__defaults__) # ('abc',)

# A dict containing defaults for keyword-only parameters.
print('kwdefaults:', Foo.method.__kwdefaults__) # None
#o#

# None or a tuple of cells that contain bindings for the function’s free variables.
# print('closure:', Foo.method.__closure__)
# A dict containing annotations of parameters. The keys of the dict are the parameter names, and
# 'return' for the return annotation, if provided.
# print('annotations:', Foo.method.__annotations__)

#!#

print(foo.method.attr1) # 'abc'
#o#

foo.method(1, 2)
#o#

#?# __func__
#?# __self__

####################################################################################################

#h# print_rule()

class FooWithNew:

    def __new__(cls, *args, **kwargs):
        print_method('FooWithNew', '__new__', cls, args, kwargs)

    def __init__(self, *args, **kwargs):
        # never called
        print_method(self, '__init__', self, args, kwargs)

#!#

foo = FooWithNew(1, 2, attr1='abc')

#o#

####################################################################################################
#!#
#!# Subclass
#!# --------

#h# print_rule()

class Bar(Foo):

    def __init__(self, *args, **kwargs):
        print_method(self, '__init__', self, args, kwargs)
        super().__init__(*args, **kwargs)

#!#

obj = Bar(1, 2, attr1='abc')

#o#

####################################################################################################
#!#
#!# Customizing Attribute Access
#!# ----------------------------

#h# print_rule()

class Attributes:

    attr1 = 1

    def __getattr__(self, name):
        print_method(self, '__getattr__', self, name)
        return None

    def __setattr__(self, name, value):
        print_method(self, '__setattr__', self, name)

    def __delattr__(self, name):
        print_method(self, '__deltattr__', self, name)

    # def __dir__(self):

#!#

obj = Attributes()
print(obj.attr1)
print(obj.foo)

#o#

####################################################################################################

class Attributes2:

    attr1 = 1

    # Fixme:
    def __getattribute__(self, name):
        print_method(self, '__getattribute__', self, name)
        raise AttributeError
        # return type.__getattribute__(self, name)
        # return object.__getattribute__(self, name)

#!#

obj = Attributes2()
#print(obj.attr1)
#obj.foo

##o#

####################################################################################################
#!#
#!# Implementing Descriptors
#!# ------------------------

#h# print_rule()

class Descriptor:

    def __init__(self, name, value):

        self._name = name
        self._value = value

    def __get__(self, instance, owner):
        print_method(self, '__get__', self, instance, owner)
        return self._value

    def __set__(self, instance, value):
        print_method(self, '_set__', self, instance, value)
        self._value = value

    def __delete__(self, instance):
        print_method(self, '__delete__', self, instance)

    def __set_name__(self, owner, name):
        print_method(self, '__set_name__', self, owner, name)


class UsingDescriptor:
    attr1 = Descriptor('attr1', 1) # class __set_name__(__main__.UsingDescriptor, 'attr1')

#!# Invoking Descriptors

obj = UsingDescriptor()
print(obj.attr1) # call __get__
obj.attr1 = 2 # call __set__
del obj.attr1 # call __delete__

#o#

####################################################################################################
#!#
#!# Slots
#!# -----

#h# print_rule()

class Slotted:

    __slots__ = ('x', 'y')

#!#

obj = Slotted()
print(obj.__slots__)
obj.x = 1 # implemented as descriptor
obj.y = 2

#o#

####################################################################################################
#!#
#!# Properties
#!# ----------

#h# print_rule()

class Property:

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def del_x(self):
        del self.__x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

####################################################################################################
#!#
#!# Customising Class Creation
#!# --------------------------

#h# print_rule()

class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        print_method(cls, '__init_subclass__', default_name, kwargs)
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name


class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass

#!#

obj = Philosopher()
obj = AustralianPhilosopher()

#o#

####################################################################################################
#!#
#!# Metaclass
#!# ---------

#h# print_rule()

class Metaclass(type):

    @classmethod
    def __prepare__(meta_cls, name, bases, **kwargs):
        print_method(meta_cls, '__prepare__', name, bases, kwargs)
        return collections.OrderedDict()

    def __new__(meta_cls, name, bases, namespace, **kwargs):
        print_method('Metaclass', '__new__', meta_cls, name, bases, namespace, kwargs)
        result = type.__new__(meta_cls, name, bases, dict(namespace))
        result.members = tuple(namespace)
        return result

    def __init__(cls, name, bases, namespace):
        # Attention: first parameter is cls, not meta_cls !
        print_method('Metaclass', '__init__', cls, name, bases, namespace)
        print_method('Metaclass', '__init__', cls.__dict__)
        type.__init__(cls, name, bases, namespace)
        # super(Metaclass, cls).__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print_method(cls, '__call__', cls, args, kwargs)
        return type.__call__(cls, *args, **kwargs)

class Metaclassed(metaclass=Metaclass):

    def __init__(self, *args, **kwargs):
        print_method(self, '__init__', self, args, kwargs)

    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass
#o#

pretty_print(Metaclassed.__dict__)
#o#

class SubMetaclassed(Metaclassed):
    pass
#o#

print(Metaclassed.members)
#o#

obj = Metaclassed(1, 2, attr1='abc')
#o#

obj = SubMetaclassed(1, 2, attr1='abc')
#o#

####################################################################################################
#!#
#!# Customising Instance and Subclass Checks
#!# ----------------------------------------

# class.__instancecheck__(self, instance)
# class.__subclasscheck__(self, subclass)

####################################################################################################
#!#
#!# Emulating Callable Objects
#!# --------------------------

#h# print_rule()

class Callable:

    def __call__(self, *args, **kwargs):
        print_method(self, '__call__', args, kwargs)

#!#

obj = Callable()
obj(1, 2, attr1='abc') # call Callable.__call__

#o#

####################################################################################################
#!#
#!# Emulating Container Types
#!# -------------------------

#h# print_rule()

class Container:

    def __init__(self, *values):
        print_method(self, '__init__', values)
        self._values = list(values) # mutable

    def __len__(self):
        print_method(self, '__len__')
        return len(self._values)

    def __length_hint__(self):
        print_method(self, '__length_hint__')
        # Called to implement operator.length_hint()
        return 10

    def __getitem__(self, key):
        print_method(self, '__getitem__', key)
        return self._values[key] # key can be a slice

    def __missing__(self, key):
        # Called by dict.__getitem__() to implement self[key] for dict subclasses when key is not in the dictionary.
        print_method(self, '__missing__')

    def __setitem__(self, key, value):
        print_method(self, '__setitem__', key, value)
        self._values[key] = value

    def __delitem__(self, key):
        print_method(self, '__delitem__', key)
        del self._values[key]

    def __iter__(self):
        print_method(self, '__iter__')
        return iter(self._values)

    def __reversed__(self):
        print_method(self, '__reversed__')
        return reversed(self._values)

    def __contains__(self, item):
        print_method(self, '__contains__', item)
        return item in self._values

#!#

obj = Container(*range(5))
print(obj[1])
obj[4] = 6
print(len(obj))
print(list(obj))
print(list(reversed(obj)))
print(1 in obj)

#o#

####################################################################################################
#!#
#!# Emulating Numeric Types
#!# -----------------------

class Numeric:

    # These methods are called to implement the binary arithmetic operations:
    # + - * @ / // % divmod() pow() ** << >> & ^ |

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __matmul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __divmod__(self, other):
        pass

    def __pow__(self, other, modulo):
        pass

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __and__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __or__(self, other):
        pass

    # These methods are called to implement the binary arithmetic operations with reflected (swapped) operands:
    # + - * @ / // % divmod() pow() ** << >> & ^ |

    def __radd__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __rmatmul__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __rfloordiv__(self, other):
        pass

    def __rmod__(self, other):
        pass

    def __rdivmod__(self, other):
        pass

    def __rpow__(self, other):
        pass

    def __rlshift__(self, other):
        pass

    def __rrshift__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __rxor__(self, other):
        pass

    def __ror__(self, other):
        pass

    # These methods are called to implement the augmented arithmetic assignments:
    # += -= *= @= /= //= %= **= <<= >>= &= ^= |=

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __imatmul__(self, other):
        pass

    def __itruediv__(self, other):
        pass

    def __ifloordiv__(self, other):
        pass

    def __imod__(self, other):
        pass

    def __ipow__(self, other, modulo):
        pass

    def __ilshift__(self, other):
        pass

    def __irshift__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __ixor__(self, other):
        pass

    def __ior__(self, other):
        pass

    # Called to implement the unary arithmetic operations:
    # - + abs() ~

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __abs__(self):
        pass

    def __invert__(self):
        pass

    # Called to implement the built-in functions complex(), int(), float() and round():

    def __complex__(self):
        pass

    def __int__(self):
        pass

    def __float__(self):
        pass

    def __round__(self, n):
        pass

    def __index__(self):
        # Called to implement operator.index()
        pass

####################################################################################################
#!#
#!# With Statement Context Managers
#!# -------------------------------

class ContextManager:

    def __init__(self, *args, **kwargs):
        print_method(self, '__init__', self, args, kwargs)

    def __enter__(self):
        print_method(self, '__enter__', self)

    def __exit__(self, exc_type, exc_value, traceback):
        print_method(self, '__exit__', self, exc_type, exc_value, traceback)

#!#

with ContextManager(1, 2, attr1='abc') as obj:
    print('here', obj)

#o#

try:
    with ContextManager(1, 2, attr1='abc') as obj:
        print('here', obj)
        raise NameError('an error')
except NameError as exception:
    print(exception)
#o#

####################################################################################################
#!#
#!# Coroutines
#!# ----------

#!# Awaitable Objects
#!# ~~~~~~~~~~~~~~~~~

# object.__await__(self)

#!# Coroutine Objects
#!# ~~~~~~~~~~~~~~~~~

# coroutine.send(value)
# coroutine.throw(type[, value[, traceback]])
# coroutine.close()

#!# Asynchronous Iterators
#!# ~~~~~~~~~~~~~~~~~~~~~~
#!#
#!# An asynchronous iterable is able to call asynchronous code in its __aiter__ implementation, and
#!# an asynchronous iterator can call asynchronous code in its __anext__ method.

class Reader:

    async def readline(self):
        pass

    def __aiter__(self):
        # Must return an asynchronous iterator object.
        return self

    async def __anext__(self):
        # Must return an awaitable resulting in a next value of the iterator.
        # Should raise a StopAsyncIteration error when the iteration is over.
        val = await self.readline()
        if val == b'':
            raise StopAsyncIteration
        return val

#!# Asynchronous Context Managers
#!# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!#
#!# An asynchronous context manager is a context manager that is able to suspend execution in its
#!# __aenter__ and __aexit__ methods.

class AsyncContextManager:

    async def __aenter__(self):
        # This method is semantically similar to the __enter__(),
        # with only difference that it must return an awaitable.
        await log('entering context')

    async def __aexit__(self, exc_type, exc, tb):
        # This method is semantically similar to the __exit__(),
        # with only difference that it must return an awaitable.
        await log('exiting context')
