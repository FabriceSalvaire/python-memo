from typing import Annotated, get_type_hints
from dataclasses import dataclass
import inspect

@dataclass
class ValueRange:
    lo: int = 1
    hi: int = 2

T1 = Annotated[int, ValueRange(-10, 5)]
T2 = Annotated[T1, ValueRange(-20, 3)]

class Foo:
    p1: T1

print(Foo.__dict__)
print(inspect.get_annotations(Foo))
print(get_type_hints(Foo, include_extras=True))
t = Foo.__annotations__['p1']
print(t.__dict__)
print(t.__origin__)
print(t.__metadata__)

# p1 is not in dict
print('p1' in Foo.__dict__)
