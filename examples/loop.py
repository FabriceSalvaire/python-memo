#!# =======
#!#  Loops
#!# =======
#!#
#!# This page contains a memo on loop statements.

#!#
#!# For Loop
#!# --------

for i in range(5):
    print(i)
else:
    print('end')
#o#

for i in range(1000):
    if 5 < i:
        break
    print(i)
else:
    print('end')
#o#

#!#
#!# While Loop
#!# ----------

i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('end')
#o#

i = 0
while i < 1000:
    if 5 < i:
        break
    print(i)
    i += 1
else:
    print('end')
#o#
