####################################################################################################

# [typing — Support for type hints — Python documentation](https://docs.python.org/3/library/typing.html)

# [Specification for the Python type system — typing documentation](https://typing.python.org/en/latest/spec/index.html)
# [Type hints cheat sheet - mypy documentation](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
# [Static Typing with Python — typing documentation](https://typing.python.org/en/latest)

# [PEP 484 – Type Hints | peps.python.org](https://peps.python.org/pep-0484)
# [PEP 585 – Type Hinting Generics In Standard Collections | peps.python.org](https://peps.python.org/pep-0585)
# [PEP 591 – Adding a final qualifier to typing | peps.python.org](https://peps.python.org/pep-0591)
# [PEP 593 – Flexible function and variable annotations | peps.python.org](https://peps.python.org/pep-0593)
# [PEP 681 – Data Class Transforms | peps.python.org](https://peps.python.org/pep-0681)
# [PEP 698 – Override Decorator for Static Typing | peps.python.org](https://peps.python.org/pep-0698)
# [PEP 742 – Narrowing types with TypeIs | peps.python.org](https://peps.python.org/pep-0742)

####################################################################################################

# Todo
#   typing.Concatenate
#   typing.Required typing.NotRequired typing.ReadOnly TypedDict

####################################################################################################

from collections.abc import Awaitable, Callable, Generator, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    ClassVar,
    Final,
    Literal,
    LiteralString,
    Never,
    NewType,
    NoReturn,
    # overload,
    Protocol,
    Self,
    TypeIs,
    TypeGuard,
)
import typing

####################################################################################################
#
# Deprecated
#

# AnyStr    3.13
# TypeAlias 3.12
#
# List...   3.9 -> buitins
#
# Iterable  3.9 -> collections.abc
# Iterator  3.9 -> collections.abc
# Callable  3.9 -> collections.abc
#
# Union     ?
# Optional  ?

####################################################################################################

# only evaluated by type checker
if TYPE_CHECKING:
    ...

####################################################################################################
#
# Union
#   now we can use `int | str` instead of `Union[int, str]`
#

x: int | str
x = 0
x = '...'

# def optional_arg(arg: Optional[int] = None) -> None:
def optional_arg(arg: int | None = None) -> None:
    ...

####################################################################################################
#
# LiteralString
#

def run_query(sql: LiteralString) -> None:
    ...

run_query('...')

####################################################################################################
#
# Literal
#

type Mode = Literal['r', 'rb', 'w', 'wb']
type OneTwoThree = Literal[1, 2, 3]

####################################################################################################
#
# Never / NoReturn
#

def stop() -> NoReturn:
    raise RuntimeError('no way')

# see also typing.assert_never()
def never_call_me(arg: Never) -> None:
    pass

####################################################################################################
#
# Self
#

class ClassSelf:
    # Warning: when subclassed
    #   use Self only if it is guaranteed to return an instance of a subclass of ClassSelf
    #   else use 'ClassSelf'
    def return_self(self) -> Self:
        return self

####################################################################################################

x: list[int] = []
# y: list[int, str] = [1, 'foo']
z: Mapping[str, str | int] = {}

####################################################################################################
#
# Type aliases
#   Python 3.12

type Vector = list[float]

####################################################################################################
#
# NewType
#

UserId = NewType('UserId', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId) -> None:
    ...


# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
# user_b = get_user_name(-1)

####################################################################################################
#
# Annotating callable objects
#
# typing.Callable is deprecated


def use_callback(callback: Callable[[int, int], str]) -> None:
    ...

def callback(a: int, b: int) -> str:
    return f"{a}-{b}"

use_callback(callback)


async def on_update(value: str) -> None:
    ...

callback: Callable[[str], Awaitable[None]] = on_update


# If a literal ellipsis ... is given as the argument list,
# it indicates that a callable with any arbitrary parameter list would be acceptable

def concat(x: str, y: str) -> str:
    return x + y

# ??? ty [invalid-declaration]: Cannot declare type `(...) -> str` for inferred type `list[int]`
x: Callable[..., str]
x = str
x = concat


# Callable cannot express complex signatures such as functions
# that take a variadic number of arguments, overloaded functions,
# or functions that have keyword-only parameters.
# However, these signatures can be expressed by defining
# a Protocol class with a __call__() method

class Combiner(Protocol):
    def __call__(self, *values: bytes, maxlen: int | None = None) -> list[bytes]: ...

def batch_processing(data: Iterable[bytes], cb_results: Combiner) -> bytes:
    return b''

def good_cb(*values: bytes, maxlen: int | None = None) -> list[bytes]:
    return [b'']

def bad_cb(*values: bytes, maxitems: int | None = None) -> list[bytes]:
    return [b'']

batch_processing([], good_cb)
# batch_processing([], bad_cb)

####################################################################################################
#
# Generics
#

# Function is generic over the TypeVar "T"
def first[T](l: Sequence[T]) -> T:
    return l[0]

# Alternative
# Declare type variable "U"
# U = TypeVar('U')
#
# def second(l: Sequence[U]) -> U:
#     return l[1]

####################################################################################################
#
# Annotating tuples
#

# tuple accepts any number of type arguments
x: tuple[int] = (5,)
y: tuple[int, str] = (5, 'foo')
# z: tuple[int] = (1, 2, 3)
# any length with same type
x: tuple[int, ...] = (1, 2)
# empty
y: tuple[()] = ()

####################################################################################################
#
# The type of class objects
#

class User: ...
class ProUser(User): ...

def make_new_user(user_class: type[User]) -> User:
    return user_class()

make_new_user(User)
make_new_user(ProUser)

####################################################################################################
#
# Annotating generators and coroutines
#

# https://docs.python.org/3/reference/expressions.html#generator-iterator-methods

# Generator[YieldType, SendType, ReturnType]
# g.next()      starts the generator or resumes it at the last executed yield expression
#               yield evaluates to None
#               returns the next yield or StopIteration
# g.send(None)  starts the generator
# g.send(value) resumes
#               yield evaluates to value
#               returns the next yield or StopIteration

def infinite_stream(start: int) -> Generator[int]:
# def infinite_stream(start: int) -> Generator[int, None, None]:
    while True:
        yield start
        start += 1

def infinite_stream2(start: int) -> Iterator[int]:
    while True:
        yield start
        start += 1

def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        _ = yield round(sent)
        if _ is None:
            sent += 1
        else:
            sent = _
    return 'Done'

g = echo_round()
print(next(g))
print(g.send(1.2))
print(next(g))
print(next(g))
print(g.send(12.3))
print(next(g))
try:
    print(g.send(-1))
except StopIteration as e:
    print(e)

# COMPLETE

####################################################################################################
#
# User-defined generic types
#

####################################################################################################
#
# Any
#

a: Any = None
a = []
a = 2

# def any_function(item):
# same as
def any_function(item: Any) -> Any:
    return None

# Use object to indicate that a value could be any type in a typesafe manner.
# Use Any to indicate that a value is dynamically typed.

####################################################################################################
#
# Nominal vs structural subtyping
#

####################################################################################################

class C1:
    cls_attr: ClassVar[int]
    attr: int
    TIMEOUT: Final[int] = 10

C1.cls_attr = 1
# C1.TIMEOUT = 11
c1 = C1()
# c1.cls_attr = 1
c1.attr = 1

####################################################################################################
#
# Annotated[<type>, <metadata1>, ...]
#

@dataclass
class ValueRange:
    lo: int
    hi: int

T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]

print(T1.__metadata__)
print(T1.__origin__)

# typing.get_type_hints(func, include_extras=True)

####################################################################################################
#
# TypeIs / TypeGuard
#

class Parent:
    pass
class Child(Parent):
    pass

# Using `-> TypeIs[NarrowedType]` tells the static type checker that for a given function:
#   The return value is a `boolean`.
#   If the return value is `True`,
#     the type of its argument is the intersection of the argument’s original type and NarrowedType.
#   If the return value is `False`,
#     the type of its argument is narrowed to exclude NarrowedType.

def is_parent(value: object) -> TypeIs[Parent]:
    return isinstance(value, Parent)

# Using `-> TypeGuard` tells the static type checker that for a given function:
#   The return value is a boolean
#   If the return value is True,
#     the type of its argument is the type inside TypeGuard

def is_str_list(values: list[object]) -> TypeGuard[list[str]]:
    '''Determines whether all objects in the list are strings'''
    return all(isinstance(x, str) for x in values)

####################################################################################################
#
# Functions and decorators
#

anumber: int = typing.cast(int, '10')

def greet(name: str) -> None:
    typing.assert_type(name, str)
    # typing.assert_type(name, int)

def int_or_str(arg: int | str) -> None:
    match arg:
        case int():
            print("It's an int")
        case str():
            print("It's a str")
        case _ as unreachable:
            typing.assert_never(unreachable)

x: int = 1
typing.reveal_type(x)

####################################################################################################
#
# Decorator to mark an object as providing dataclass-like behavior.
#

# @typing.dataclass_transform(
#   *,
#   eq_default=True,
#   order_default=False,
#   kw_only_default=False,
#   frozen_default=False,
#   field_specifiers=(),
#   **kwargs
# )
@typing.dataclass_transform()
def create_model[T](cls: type[T]) -> type[T]:
    return cls

@create_model
class CustomerModel:
    id: int
    name: str

####################################################################################################
#
# Overload
#

@typing.overload
def process(response: None) -> None:
    ...
@typing.overload
def process(response: int) -> tuple[int, str]:
    ...
@typing.overload
def process(response: bytes) -> str:
    ...

def process(response):
    ...  # actual implementation goes here

typing.get_overloads(process)
# Clear all registered overloads in the internal registry
typing.clear_overloads()


class Base:
    @typing.final
    def done(self) -> None:
        ...
# class Sub(Base):
#     def done(self) -> None:
#         ...

@typing.final
class Leaf:
    ...
# class Other(Leaf):
#     ...

####################################################################################################

# Decorator to indicate that annotations are not type hints
# @typing.no_type_check

####################################################################################################

