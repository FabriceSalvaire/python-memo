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

#l# async for TARGET in ITER:
#l#     # do something
#l#     pass
#l# else:
#l#     # else do something
#l#     pass

#!#
#!# The async with statement
#!# ------------------------

#l# async with EXPR as VAR:
#l#     # do something
#l#     pass
