####################################################################################################

# [PEP 622 – Structural Pattern Matching | peps.python.org](https://peps.python.org/pep-0622/#combining-multiple-patterns-or-patterns)
# [PEP 634 – Structural Pattern Matching: Specification | peps.python.org](https://peps.python.org/pep-0634)
# [PEP 635 – Structural Pattern Matching: Motivation and Rationale | peps.python.org](https://peps.python.org/pep-0635)
# [PEP 636 – Structural Pattern Matching: Tutorial | peps.python.org](https://peps.python.org/pep-0636)
# [Structural pattern matching in Python 3.10](https://benhoyt.com/writings/python-pattern-matching/)

####################################################################################################

# Use variable names that are set if a case matches
# Match sequences using list or tuple syntax (like Python’s existing iterable unpacking feature)
# Match mappings using dict syntax
# Use * to match the rest of a list
# Use ** to match other keys in a dict
# Match objects and their attributes using class syntax
# Include “or” patterns with |
# Capture sub-patterns with as
# Include an if “guard” clause

####################################################################################################

from dataclasses import dataclass
from enum import Enum

####################################################################################################

# Literal Patterns
#   to filter constant values in a structure
#   It uses `__eq__`
#     thus True and 1 (or False and 0) cannot be distinguished
#   Literal values are compared with the `==` operator
#   except for the constants True, False and None which are compared with the `is` operator.

for value in (
        None,
        True,
        -1,
        1,
        1.,
        1-1j,   # complex
        'foo',
):
    match value:
        case None:
            print('value is None')
        case True:   # or False
            print('value is True')
        # Number
        case -1:
            print('value is a negative integer')
        case 1:
            print('value is integer')
        case 1.:
            print('value is float')
        case 1-1j:
            print('value is complex number')
        # String
        case 'foo':
            print('value is string')
        # triple quote is also allowed

####################################################################################################

# Capture Patterns
# (???) A capture pattern looks like x and is equivalent to an identical assignment target:
#   it always matches and binds the variable with the given (simple) name.

for greeting in (
        '',
        'bob',
):
    match greeting:
        case '':
            print("Hello!")
        case name:
            # makes the name local to that scope
            print(f"Hi {name}!")

####################################################################################################

# Wildcard Pattern
#   The wildcard pattern is a single underscore: _
#   It always matches, but does not capture any variable
#   (which prevents interference with other uses for _ and allows for some optimizations)

for value in (
        ('a', 'b'),
):
    match value:
        case (_, _):
            print('value is a pair')

####################################################################################################

# Constant Value Patterns
#   A constant value pattern works like the literal but for certain named constants.
#   Note that it must be a qualified (dotted) name, given the possible ambiguity with a capture pattern.
#   It never binds.

class Sides(str, Enum):
    SPAM = 'Spam'
    EGGS = 'eggs'

for value in (
        Sides.SPAM,
        Sides.EGGS,
):
    match value:
        case Sides.SPAM:   # Compares value == Sides.SPAM.
            response = "Have you got anything without Spam?"
        case side:   # Assigns side = calue
            response = f"Well, could I have their Spam instead of the {side} then?"
    print(response)

####################################################################################################

# Sequence Patterns
#   A sequence pattern looks like [a, *rest, b] and is similar to a list unpacking.
#   An important difference is that the elements nested within it can be any kind of patterns,
#   not just names or sequences.
#   It matches only sequences of appropriate length, as long as all the sub-patterns also match.
#   It makes all the bindings of its sub-patterns.
#
#   To match a sequence pattern the subject must be an instance of `collections.abc.Sequence`,
#   and it cannot be any kind of string (str, bytes, bytearray).
#   It cannot be an iterator.
#
#   [*_] matches a sequence of any length
#   (_, _, *_), matches any sequence of length two or more
#   ['a', *_, 'z'] matches any sequence of length two or more that starts with 'a' and ends with 'z'

for value in (
        ('a', 'b'),
        (1, 'foo'),
        (1, ['a', 'b', 'c']),
        ('a', 'b', 'c', 'z'),
):
    match value:
        case ('a', 'b'):
            print('value is (a, b)')
        case (1, x):
            print(f"Got 1 and {x}")
        case 1, [x, *others]:
            print(f"Got 1 and a nested sequence [{x}, {others}]")
        case ['a', *_, 'z']:
            print("Got [a, ..., z]")

####################################################################################################

# Mapping Patterns
#   A mapping pattern looks like {"user": u, "emails": [*es]}
#   It matches mappings with at least the set of provided keys,
#   and if all the sub-patterns match their corresponding values.
#   It binds whatever the sub-patterns bind while matching with the values corresponding to the keys.
#   Adding **rest at the end of the pattern to capture extra items is allowed.
#
#   must be an instance of collections.abc.Mapping
#   Matched key-value pairs must already be present in the mapping,
#   and not created on-the-fly by __missing__ or __getitem__.
#   For example, collections.defaultdict instances will only match patterns with keys
#   that were already present when the match block was entered.

for value in (
        {'a': 1},
        {'a': 1, 'b': 2},   # extra keys are ignored even if **rest is not present
        {'b': 1, 'c': 2},
):
    match value:
        case {'a': number}:
            print(f"value is {{ a: {number} }}")
        case {'b': number, **rest}:
            print(f"value is {{ b: {number}, {rest} }}")

####################################################################################################

# Class Pattern
#   A class pattern is similar to the above but matches attributes instead of keys.
#   It looks like datetime.date(year=y, day=d).
#   It matches instances of the given type, having at least the specified attributes,
#   as long as the attributes match with the corresponding sub-patterns.
#   It binds whatever the sub-patterns bind when matching with the values of the given attributes.
#   An optional protocol also allows matching positional arguments.
#
#  A class pattern provides support for destructuring arbitrary objects.
#  There are two possible ways of matching on object attributes: by position like Point(1, 2),
#  and by name like Point(x=1, y=2).
#  These two can be combined, but a positional match cannot follow a match by name.
#
#  Whether a match succeeds or not is determined by the equivalent of an isinstance call.

@dataclass
class Point:
    x: float
    y: float


class Point2d:
    # special attribute to define an explicit order for attributes that can be used in patterns
    __match_args__ = ('x', 'y')

    # here we use a _ suffix for kwargs in order to avoid confusion
    def __init__(self, x_: float, y_: float) -> None:
        self.x = x_
        self.y = y_

    def __repr__(self) -> str:
        return f'Point2d({self.x}, {self.y})'


class Point3d:
    __match_args__ = ('x', 'y', 'z')

    def __init__(self, x_: float, y_: float, z_: float) -> None:
        self.x = x_
        self.y = y_
        self.z = z_

    def __repr__(self) -> str:
        return f'Point3d({self.x}, {self.y}, {self.z})'


def make_point_3d(pt):
    match pt:
        case (x, y):
            return Point3d(x, y, 0)
        case (x, y, z):
            return Point3d(x, y, z)
        # test if isinstance(pt, Point2d)
        # then match attributes
        # Notice that x is a class attribute an not the key argument !
        case Point(x, y):
            return Point3d(x, y, 0)
        case Point2d(x, y):
        # or
        # case Point2d(x=x, y=y):
            return Point3d(x, y, 0)
        case Point3d(x=_, y=2, z=_):
        # SyntaxError: case Point3d(_, y=2, _):
            return pt
        case Point3d():
        # same as
        # case Point3d(_, _, _):
            return pt
        case _:
            raise TypeError("not a point we support")


for value in (
    (1, 2),
    (1, 2, 3),
    Point(1, 4),
    Point2d(1, 2),
    Point3d(1, 2, 3),
    Point3d(1, 3, 3),
    ):
    print(make_point_3d(value))

####################################################################################################

# Combining multiple patterns (OR patterns)
#   An OR pattern looks like [*x] | {"elems": [*x]}.
#   It matches if any of its sub-patterns match.
#   It uses the binding for the leftmost pattern that matched.

for value in (
        1,
        [1],
        'foo',
        None,
):
    match value:
        case 0 | 1 | 2:
            print("Small number")
        case [] | [_]:
            print("A short sequence")
        case str() | bytes():
            print("Something string-like")
        case _:
            print("Something else")

# The alternatives may bind variables,
# as long as each alternative binds the same set of variables (excluding _)

for value in (
        1,
        [2],
        Point2d(1, 2),
):
    match value:
        # SyntaxError:
        # case 1 | x:
        # case x | 1:
        case Point2d(x, y) | Point3d(x, y, 0):
            print(f"value is Point ({x}, {y}, 0)")
        case [x] | x:
            print(f"value is {x}")

####################################################################################################

# Guards

for value in (
        1,
        11,
        (11, 12),
):
    match value:
        case int(x) if x > 10:
            print('value is > 10')
        case (x, y) if x > 10 and y > 10:
            print('value is pair > 10')

####################################################################################################

# as (Walrus) patterns
#   The as-pattern matches whatever pattern is on its left-hand side, but also binds the value to a name.
#   old PEP
#     A walrus pattern looks like d := datetime(year=2020, month=m)
#     It matches only if its sub-pattern also matches.
#     It binds whatever the sub-pattern match does, and also binds the named variable to the entire object.

class Line:
    __match_args__ = ('start', 'stop')
    def __init__(self, p0: Point2d, p1: Point2d) -> None:
        self.start = p1
        self.stop = p1

for p0, p1 in (
        (Point2d(1, 1), Point2d(1, 1)),
):
    match Line(p0, p1):
        case Line(Point2d(x, y) as start, end) if start == end:
            print(f"Zero length line at {x}, {y}")

####################################################################################################

# Matching builtin classes (e.g. bool, str, int, float)

for value in (
        {'text': 'hello', 'color': 'blue'},
        {'sleep': 1.},
):
    match value:
        # `str(c)` is a shorthand  for `str() as c`
        case {'text': str(message), 'color': str(c)}:
            print(f"{message} {c}")
        case {'sleep': float(duration)}:
            print(f"sleep {duration}")
