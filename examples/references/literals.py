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

#<i#
1_000_000_000_000_000
0x_FF_FF_FF_FF
#i>#

#<i#
'{:_}'.format(1000000)
'{:_x}'.format(0xFFFFFFFF)
#i>#
