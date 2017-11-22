#!# ===========
#!#  Unpacking
#!# ===========
#!#
#!# This page contains a memo on unpacking.

#!# `PEP 448 - Additional Unpacking Generalizations <https://www.python.org/dev/peps/pep-0448>`_

_= *[1], *[2], 3, *[4, 5]
print(_)
#o#

def fn(a, b, c, d):
    print(a, b, c, d)

fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})
#o#

_ = *range(4), 4
print(_)
_ = [*range(4), 4]
print(_)
_ = {*range(4), 4, *(5, 6, 7)}
print(_)
_ = {'x': 1, **{'y': 2}}
print(_)
#o#
