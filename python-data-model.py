####################################################################################################
#
# https://docs.python.org/3/reference/datamodel.html
#
####################################################################################################

####################################################################################################

import collections

####################################################################################################

def format_method_name(obj, method_name):
    if isinstance(obj, str):
        return obj + '.' + method_name
    else:
        return obj.__class__.__name__ + '.' + method_name

def print_method(obj, method_name, *args):
    print(format_method_name(obj, method_name), *args)

def print_rule():
    print('\n')
    print('#'*100)
    print('\n')

####################################################################################################
#
# At __main__ level
#

a_global = 1

print('At Global level:')
print('file:', __file__)
print()

####################################################################################################
#
# Basic customization
#

print_rule()

class FooWithNew:

    def __new__(cls, *args, **kwargs):
        print_method('FooWithNew', '__new__', cls, args, kwargs)

    def __init__(self, *args, **kwargs):
        # never called
        print_method(self, '__init__', self, args, kwargs)


foo = FooWithNew(1, 2, attr1='abc')

####################################################################################################

print_rule()

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


foo = Foo(1, 2, attr1='abc')

print('\nFoo Class:')
print('doc:', Foo.__doc__)
print('dict:', Foo.__dict__)

print('\nFoo.method Method:')
print('doc:', Foo.method.__doc__)
print('name:', Foo.method.__name__) # method
print('qualname:', Foo.method.__qualname__) # Foo.method
print('module:', Foo.method.__module__) # __main__
print('code:', Foo.method.__code__)
print('globals:', Foo.method.__globals__)

# A tuple containing default argument values for those arguments that have defaults, or None if no
# arguments have a default value
print('defaults:', Foo.method.__defaults__) # ('abc',)

# A dict containing defaults for keyword-only parameters.
print('kwdefaults:', Foo.method.__kwdefaults__) # None

print(foo.method.attr1) # 'abc'

# None or a tuple of cells that contain bindings for the function’s free variables.
# print('closure:', Foo.method.__closure__)
# A dict containing annotations of parameters. The keys of the dict are the parameter names, and
# 'return' for the return annotation, if provided.
# print('annotations:', Foo.method.__annotations__)

# __func__
# __self__

foo.method(1, 2)

####################################################################################################
#
# Subclass
#

print_rule()

class Bar(Foo):

    def __init__(self, *args, **kwargs):
        print_method(self, '__init__', self, args, kwargs)
        super().__init__(*args, **kwargs)


obj = Bar(1, 2, attr1='abc')

####################################################################################################
#
# Customizing attribute access
#

print_rule()

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


obj = Attributes()
print(obj.attr1)
print(obj.foo)

####################################################################################################

class Attributes2:

    attr1 = 1

    # Fixme:
    def __getattribute__(self, name):
        print_method(self, '__getattribute__', self, name)
        raise AttributeError
        # return type.__getattribute__(self, name)
        # return object.__getattribute__(self, name)


obj = Attributes2()
# print(obj.attr1)
#obj.foo

####################################################################################################
#
# Implementing Descriptors
#

print_rule()

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

# Invoking Descriptors

obj = UsingDescriptor()
print(obj.attr1) # call __get__
obj.attr1 = 2 # call __set__
del obj.attr1 # call __delete__

####################################################################################################

print_rule()

class Slotted:

    __slots__ = ('x', 'y')


obj = Slotted()
print(obj.__slots__)
obj.x = 1 # implemented as descriptor
obj.y = 2

####################################################################################################

print_rule()

class Property:

    def get_x(self):
        return self.__x

    def set_x(self, value):
        self.__x = value

    def del_x(self):
        del self.__x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

####################################################################################################
#
#  Customizing class creation
#

print_rule()

class Philosopher:
    def __init_subclass__(cls, default_name, **kwargs):
        print_method(cls, '__init_subclass__', default_name, kwargs)
        super().__init_subclass__(**kwargs)
        cls.default_name = default_name


class AustralianPhilosopher(Philosopher, default_name="Bruce"):
    pass


obj = Philosopher()
obj = AustralianPhilosopher()

####################################################################################################
#
# Metaclass
#

print_rule()

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


class Metaclassed(metaclass=Metaclass):
    def one(self): pass
    def two(self): pass
    def three(self): pass
    def four(self): pass

class SubMetaclassed(Metaclassed):
    pass


print(Metaclassed.members)
# obj = Metaclassed()

####################################################################################################
#
# Customizing instance and subclass checks
#

# class.__instancecheck__(self, instance)
# class.__subclasscheck__(self, subclass)

####################################################################################################
#
# Emulating callable objects
#

print_rule()

class Callable:

    def __call__(self, *args, **kwargs):
        print_method(self, '__call__', args, kwargs)

obj = Callable()
obj(1, 2, attr1='abc') # call Callable.__call__

####################################################################################################
#
# Emulating container types
#

print_rule()

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


obj = Container(*range(5))
print(obj[1])
obj[4] = 6
print(len(obj))
print(list(obj))
print(list(reversed(obj)))
print(1 in obj)

####################################################################################################
#
# Emulating numeric types
#

class Numeric:

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

    def __neg__(self):
        pass

    def __pos__(self):
        pass

    def __abs__(self):
        pass

    def __invert__(self):
        pass

    def __complex__(self):
        pass

    def __int__(self):
        pass

    def __float__(self):
        pass

    def __round__(self, n):
        pass

    def __index__(self):
        pass

