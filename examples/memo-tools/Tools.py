#r# ====================
#r#  Pretty Print Tools
#r# ====================
#r#
#r# This page contains the code of the pretty functions.

#?# Fixme: file order ???

####################################################################################################

__all__ = [
    'pretty_print',
    'print_function',
    'print_method',
    'print_rule',
]

####################################################################################################

import pprint

####################################################################################################

def format_method_name(obj, method_name):
    if isinstance(obj, str):
        return obj + '.' + method_name
    else:
        return obj.__class__.__name__ + '.' + method_name

def pretty_print(*args):
    pretty_printer = pprint.PrettyPrinter(indent=4, width=40, compact=False)
    for arg in args:
        for line in pretty_printer.pformat(arg).split('\n'):
            print(' '*4 + line)

def print_function(func_name, *args):
    print('@' + func_name)
    pretty_print(*args)

def print_method(obj, method_name, *args):
    print('@' + format_method_name(obj, method_name))
    pretty_print(*args)

def print_rule():
    pass
    # print('\n')
    # print('#'*100)
    # print('\n')
