# Fixme: double title

#!# ======
#!#  Math
#!# ======
#!#
#!# This page contains a memo on math functions.
#!#

import math

#!# PEP 485: A function for testing approximate equality

_= math.isclose(5.0, 4.99998, rel_tol=1e-5)
print(_)
#o#
