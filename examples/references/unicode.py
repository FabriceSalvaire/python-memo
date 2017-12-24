#r# =========
#r#  Unicode
#r# =========
#r#
#r# This page contains a memo on unicode.

####################################################################################################

_ = 'éàèù'.encode('utf-8')
print(_)
#o#

_ = _.decode('utf-8')
print(_)
#o#
