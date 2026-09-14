####################################################################################################

def function(p1: int, p2: float, p3: str = 'foo') -> int:
    "A function"
    return p1
function.foo = 1

print(function.__name__)
print(function.__qualname__)
print(function.__module__)

print(function.__doc__)

print(function.__code__)

print(function.__defaults__)
print(function.__kwdefaults__)
print(function.__type_params__)

print(function.__annotations__)

print(function.__dict__)

print(function.foo)

####################################################################################################
