####################################################################################################

# __main__ A_GLOBAL is undefined
# print(A_GLOBAL)
print('amodule locals', locals())
print('amodule globals', globals())
print('amodule dir', dir())

####################################################################################################

import sys

from rich import print

####################################################################################################

# Get main.py
_main = sys.modules['__main__']
print(f"import module {_main}")

# Get current module
_this_module = sys.modules[__name__]
print(f"import module {__name__} {_this_module}")

####################################################################################################

# starts with a _ : not imported by all
_attribute_a = 12

# module global
ATTRIBUTE_A = 123

def afunc():
    # ATTRIBUTE_A is a module global
    print(f'afunc: ATTRIBUTE_A = {ATTRIBUTE_A}')

def init_attribute1():
    # create a local variable to the func scope
    ATTRIBUTE_A = 1234

def init_attribute2():
    # ATTRIBUTE_A is a module global
    global ATTRIBUTE_A
    ATTRIBUTE_A = 12345

def init_attribute3():
    _this_module.ATTRIBUTE_A = 123456

def func_global1():
    # bin a new module global ATTRIBUTE_B if necessary
    global ATTRIBUTE_B
    ATTRIBUTE_B = 12
    foo = 1
    print(f'func_global1: ATTRIBUTE_B = {ATTRIBUTE_B}')

def func_global2():
    global ATTRIBUTE_B
    ATTRIBUTE_B = 123
    print(f'func_global1: ATTRIBUTE_B = {ATTRIBUTE_B}')
