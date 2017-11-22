#!# ============
#!#  Coroutines
#!# ============
#!#
#!# This page contains a memo on coroutines.
#!#
#!# For a complete reference documentation, look at
#!# https://docs.python.org/3/reference/compound_stmts.html#coroutines and `PEP 492 -- Coroutines
#!# with async and await syntax <https://www.python.org/dev/peps/pep-0492>`_.

####################################################################################################

from Tools import *

####################################################################################################

#!#
#!# **To be completed**

#!#
#!# Coroutine function definition
#!# -----------------------------

async def func(param1, param2):
    do_stuff()
    await some_coroutine()

#!#
#!# The async for statement
#!# -----------------------

#!# .. code-block:: py3
#!#
#!#     async for TARGET in ITER:
#!#         # do something
#!#         pass
#!#     else:
#!#         # else do something
#!#         pass

#!#
#!# The async with statement
#!# ------------------------

#!# .. code-block:: py3
#!#
#!#     async with EXPR as VAR:
#!#         # do something
#!#         pass
