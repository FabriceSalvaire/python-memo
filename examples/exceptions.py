#!# ============
#!#  Exceptions
#!# ============
#!#
#!# This page contains a memo on exceptions.
#!#
#!# For a complete reference documentation, look at https://docs.python.org/3/reference/compound_stmts.html#try

try:
    x = 1 / 0
except ZeroDivisionError as exception:
    print(type(exception), exception)
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

try:
    x = 1 / 1
except Exception as exception:
    print(exception)
finally:
    print('try block succeed')
#o#

