# Built-in Functions

https://docs.python.org/3/library/functions.html

A
abs()
aiter()
all()
anext()
any()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()
	
E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input()
int()
isinstance()
issubclass()
iter()
	
L
len()
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open()
ord()

P
pow()
print()
property()
	
R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()

# Data Model

For CPython, id(x) is the memory address where x is stored.

## Callable types

function.__globals__
function.__closure__

function.__doc__
function.__name__
function.__qualname__
function.__module__
function.__defaults__
function.__code__
function.__dict__
function.__annotations__
function.__kwdefaults__
function.__type_params__ generic function

# Instance methods

 method.__self__
 method.__func__
 method.__doc__
 method.__name__
 method.__module__
 
 ## Module
 
 module.__name__
 module.__spec__
 module.__package__
 module.__loader__
 module.__path__
 module.__file__
 module.__cached__
 module.__doc__
 module.__annotations__
 module.__dict__
 
 # Custom classes
 
 type.__name__
 type.__qualname__
 type.__dict__
 type.__bases__ tuple containing the class’s bases
 type.__doc__
 type.__annotations__ but use inspect.get_annotations()
 type.__type_params__ generic class
 type.__static_attributes__
    stores the names of attributes accessed through self.X in any function in a class body.
   A tuple containing names of attributes of this class which are assigned through self.X from any function in its body.
 type.__firstlineno__
 type.__mro__ method resolution
 
 type.mro()
 type.__subclasses__()
  
# Class instances

object.__class__
object.__dict__

# Special method names

## Basic customization

object.__new__(cls[, ...])
object.__init__(self[, ...])

object.__del__(self)

object.__repr__(self)
object.__str__(self)
object.__bytes__(self)
object.__format__(self, format_spec)

object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)

object.__hash__(self)
object.__bool__(self)

# Customizing attribute access

object.__getattr__(self, name)
object.__getattribute__(self, name)
object.__setattr__(self, name, value)
object.__delattr__(self, name)
object.__dir__(self)

# Customizing module attribute access

[PEP 562 – Module __getattr__ and __dir__ | peps.python.org](https://peps.python.org/pep-0562/)

__getattr__
__dir__

# Descriptors

object.__get__(self, instance, owner=None)
object.__set__(self, instance, value)
object.__delete__(self, instance)
object.__objclass__

# slots

 object.__slots__

# Customizing class creation

object.__init_subclass__(cls)
object.__set_name__(self, owner, name)

# Metaclasses

__prepare__
object.__mro_entries__(self, bases)

