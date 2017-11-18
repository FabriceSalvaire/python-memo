#!# ==================
#!#  Lexical Analysis
#!# ==================
#!#
#!# This page contains a memo on lexical analysis.
#!#
#!# For a complete reference documentation, look at https://docs.python.org/3.6/reference/lexical_analysis.html

#!#
#!# Python Keywords
#!# ---------------
#!#
#!# .. code-block:: py3
#!#
#!#     False      class      finally    is         return
#!#     None       continue   for        lambda     try
#!#     True       def        from       nonlocal   while
#!#     and        del        global     not        with
#!#     as         elif       if         or         yield
#!#     assert     else       import     pass
#!#     break      except     in         raise

#!#
#!# Reserved classes of identifiers
#!# -------------------------------
#!#
#!# :code:`_*`
#!#     Not imported by from module import *
#!# :code:`__*__`
#!#     System-defined names
#!# :code:`__*`
#!#     Class-private names
#!#
#!# Usually, :code:`_` is assigned to last evaluation or used in conjunction with *gettext* for internationalization.

#!#
#!# Indentation
#!# -----------

#!# Using continuation, backslash character "\\":

def check_date(year, month, day, hour, minute, second):
    if 1900 < year < 2100 and 1 <= month <= 12 \
       and 1 <= day <= 31 and 0 <= hour < 24 \
       and 0 <= minute < 60 and 0 <= second < 60:
        return True

#!# Better, using parenthesis, brace and bracket:

def check_date(year, month, day, hour, minute, second):
    if (1900 < year < 2100 and 1 <= month <= 12
        and 1 <= day <= 31 and 0 <= hour < 24
        and 0 <= minute < 60 and 0 <= second < 60):
        return True

x = (1 +
     2 * 3 -
     4 / 6)
