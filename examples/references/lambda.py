#r# ====================
#r#  Lambda Expressions
#r# ====================
#r#
#r# This page contains a memo on lambda expressions.

#r#
#r# A lambda expressions is an anonymous function:

multiply_by_two = lambda x: x*2

print(multiply_by_two(2))
#o#

#r# which is equivalent to

def multiply_by_two(x):
    return x*2

#r# But permit shorter syntactic construction like

unsorted = [(x, i) for i, x in enumerate((3, 5, 4, 1, 2))]
print(unsorted)
#o#

sorted_list = sorted(unsorted, key=lambda x: x[0])
print(sorted_list)
#o#
