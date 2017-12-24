#r# =============
#r#  Comparisons
#r# =============
#r#
#r# This page contains a memo on comparisons.

####################################################################################################

from Tools import *

####################################################################################################

#r# Let define some strings

s0 = 'abc'
s1 = 'def'

#r# Let define a reference or alias to :code:`s0`

s2 = s0

#r# :code:`s0` and :code:`s2` have the same *id*, address of the object in memory.

pretty_print([id(x) for x in (s0, s2, s1)])
#o#

print(id(s0) == id(s2))
#o#

#r# Equality Test
#r# -------------

print(s0 != s1)
#o#

print(s0 == s2)
#o#

#r# Reference Test
#r# --------------

print(s0 is not s1)
#o#

print(s0 is s2)
#o#

#r# Comparison Tests
#r# ----------------

x = 2
print(0 <= x < 10)
#o#

#r# shorter than

0 <= x and x < 10
