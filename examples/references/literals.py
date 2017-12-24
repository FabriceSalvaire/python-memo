#r# ===========
#r#  Litterals
#r# ===========
#r#
#r# This page contains a memo on litterals.

####################################################################################################

from Tools import *

####################################################################################################

#r#
#r# Underscores in Numeric Literals
#r# -------------------------------
#r#
#r# :frompy:`3.6`
#r#
#r# `PEP 515 - Underscores in Numeric Literals <https://www.python.org/dev/peps/pep-0515>`_

#<i#
1_000_000_000_000_000
0x_FF_FF_FF_FF
#i>#

#<i#
'{:_}'.format(1000000)
'{:_x}'.format(0xFFFFFFFF)
#i>#
