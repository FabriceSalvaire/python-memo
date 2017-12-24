#r# ============
#r#  Coroutines
#r# ============
#r#
#r# This page contains a memo on coroutines.
#r#
#r# For a complete reference documentation, look at
#r# https://docs.python.org/3/reference/compound_stmts.html#coroutines and `PEP 492 -- Coroutines
#r# with async and await syntax <https://www.python.org/dev/peps/pep-0492>`_.

####################################################################################################

from Tools import *

####################################################################################################

#r#
#r# **To be completed**

#r#
#r# Coroutine function definition
#r# -----------------------------

async def func(param1, param2):
    do_stuff()
    await some_coroutine()

#r#
#r# The async for statement
#r# -----------------------

#l# async for TARGET in ITER:
#l#     # do something
#l#     pass
#l# else:
#l#     # else do something
#l#     pass

#r#
#r# The async with statement
#r# ------------------------

#l# async with EXPR as VAR:
#l#     # do something
#l#     pass
