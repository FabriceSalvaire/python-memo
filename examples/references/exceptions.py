#r# ============
#r#  Exceptions
#r# ============
#r#
#r# This page contains a memo on exceptions.
#r#
#r# For a complete reference documentation, look at https://docs.python.org/3/reference/compound_stmts.html#try

from Tools import *

#r#
#r# Catch exceptions using :code:`try` block:

try:
    x = 1 / 0
except ZeroDivisionError as exception:
    pretty_print((exception, exception.__traceback__))
except ZeroDivisionError:
    # If we don't need the exception instance
    print('try block failed')
except Exception as exception:
    # Catch all exceptions
    print(exception)
except:
    # Shorter form to catch all exceptions
    pass # simply ignore the exception
#o#

#r#
#r# Use :code:`finally` to do cleanup:

try:
    x = 1 / 1
except Exception as exception:
    print(exception)
finally:
    print('try block succeed')
#o#

#r#
#r# Raise exceptions:

try:
    raise NameError("Something bad happened")
except Exception as exception:
    print(exception)
#o#

try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise # last exception
except Exception as exception:
    print(exception)
#o#

#r#
#r# Chain exceptions:

try:
    try:
        1 / 0
    except ZeroDivisionError as exception:
        raise NameError("Something bad happened") from exception
except Exception as exception:
    print(exception, ', caused by:', exception.__cause__)
#o#

#r# **To be completed:** :code:`exception.__context__`
