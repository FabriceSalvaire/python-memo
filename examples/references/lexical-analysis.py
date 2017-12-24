#r# ==================
#r#  Lexical Analysis
#r# ==================
#r#
#r# This page contains a memo on lexical analysis.
#r#
#r# For a complete reference documentation, look at https://docs.python.org/3.6/reference/lexical_analysis.html

#r#
#r# Python Keywords
#r# ---------------
#r#
#r# .. code-block:: py3
#r#
#r#     False      class      finally    is         return
#r#     None       continue   for        lambda     try
#r#     True       def        from       nonlocal   while
#r#     and        del        global     not        with
#r#     as         elif       if         or         yield
#r#     assert     else       import     pass
#r#     break      except     in         raise

#r#
#r# Reserved classes of identifiers
#r# -------------------------------
#r#
#r# :code:`_*`
#r#     Not imported by from module import *
#r# :code:`__*__`
#r#     System-defined names
#r# :code:`__*`
#r#     Class-private names
#r#
#r# Usually, :code:`_` is assigned to last evaluation or used in conjunction with *gettext* for internationalization.

#r#
#r# Indentation
#r# -----------

#r# Using continuation, backslash character "\\":

def check_date(year, month, day, hour, minute, second):
    if 1900 < year < 2100 and 1 <= month <= 12 \
       and 1 <= day <= 31 and 0 <= hour < 24 \
       and 0 <= minute < 60 and 0 <= second < 60:
        return True

#r# Better, using parenthesis, brace and bracket:

def check_date(year, month, day, hour, minute, second):
    if (1900 < year < 2100 and 1 <= month <= 12
        and 1 <= day <= 31 and 0 <= hour < 24
        and 0 <= minute < 60 and 0 <= second < 60):
        return True

x = (1 +
     2 * 3 -
     4 / 6)
