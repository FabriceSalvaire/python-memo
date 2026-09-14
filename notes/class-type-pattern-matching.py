from dataclasses import dataclass
import collections
import dataclasses

class A:
    class AA:
        pass

class B(A):
    pass

@dataclass
class MyClass:
    foo: int
    bar: str

def match_class_type(cls):
    match cls:
        case __builtins__.int:
            print("  is int")
        case __builtins__.str:
            print("  is str")
        case A.AA:
            print("  is A.AA")
        case collections.Counter:
            print("  is Counter")
        case _:
            print("  _")
    match cls.__qualname__:
        case int.__qualname__:
            print("  is int")
        case str.__qualname__:
            print("  is str")
        case A.__qualname__:
            print("  is A")
        case A.AA.__qualname__:
            print("  is A.AA")
        case B.__qualname__:
            print("  is B")
        case _:
            print("  _")

print("Class A")
match_class_type(A)
print("Class B")
match_class_type(B)

print("Class A.AA")
match_class_type(A.AA)
print("collections.Counter")
match_class_type(collections.Counter)

for _ in dataclasses.fields(MyClass):
    print(f"{_.name} {_.type}")
    match_class_type(_.type)
