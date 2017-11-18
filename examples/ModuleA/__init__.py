#skip#

print('Building ModuleA')

try:
    print(a_global)
except NameError as exception:
    print(exception)

try:
    print(__main__.a_global) # wrong
except NameError as exception:
    print(exception)
