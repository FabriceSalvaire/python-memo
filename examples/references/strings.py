#r# =========
#r#  Strings
#r# =========
#r#
#r# This page contains a memo on strings.

####################################################################################################

import decimal

from Tools import *

####################################################################################################

#r#
#r# Formatted string literals
#r# -------------------------
#r#
#r# :frompy:`3.6`
#r#
#r# `PEP 498 - Formatted string literals <https://www.python.org/dev/peps/pep-0498>`_

name = "Fred"
print(f"He said his name is {name}.")
#o#

width = 10
precision = 4
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}") # nested fields
#o#

