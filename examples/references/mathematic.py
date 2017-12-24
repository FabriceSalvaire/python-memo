# Fixme: double title

#r# ======
#r#  Math
#r# ======
#r#
#r# This page contains a memo on math functions.
#r#

import math

#r# PEP 485: A function for testing approximate equality

_= math.isclose(5.0, 4.99998, rel_tol=1e-5)
print(_)
#o#
