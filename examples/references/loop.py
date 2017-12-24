#r# =======
#r#  Loops
#r# =======
#r#
#r# This page contains a memo on loop statements.

#r#
#r# For Loop
#r# --------

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

for i in range(100):
    if not (10 < i < 16):
        continue
    print(i)
else:
    print('end')
#o#


#r#
#r# While Loop
#r# ----------

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
