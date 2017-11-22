#!# ===========
#!#  Litterals
#!# ===========
#!#
#!# This page contains a memo on litterals.

####################################################################################################

from Tools import *

####################################################################################################

#!#
#!# Underscores in Numeric Literals
#!# -------------------------------
#!#
#!# :frompy:`3.6`
#!#
#!# `PEP 515 - Underscores in Numeric Literals <https://www.python.org/dev/peps/pep-0515>`_

a_int = 1_000_000_000_000_000
a_hex = 0x_FF_FF_FF_FF
print(a_int, a_hex)
#o#

a_int = '{:_}'.format(1000000)
a_hex = '{:_x}'.format(0xFFFFFFFF)
print(a_int, a_hex)
#o#
