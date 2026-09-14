# Import

- [Import statement — Python documentation](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement)
- [Package Relative Import — Python documentation](https://docs.python.org/3/reference/import.html#relativeimports)

```py
# import <>
import foo                  # foo imported and bound locally
import foo.bar.baz          # foo, foo.bar, and foo.bar.baz imported, foo bound locally
import foo.bar.baz as fbb   # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as fbb
# from <> import <>
from foo.bar import baz     # foo, foo.bar, and foo.bar.baz imported, foo.bar.baz bound as baz
from foo import attr        # foo imported and foo.attr bound as attr

# from <> import *
from foo import *   # -> __all__ = ['...', ...]

# Relative imports
#   one dot means current package
#   two dots means parent parent
#   three dots ...
#
# package/
#     __init__.py
#     subpackage1/
#         __init__.py
#         moduleX.py
#         moduleY.py
#     subpackage2/
#         __init__.py
#         moduleZ.py
#     moduleA.py
# In either subpackage1/moduleX.py or subpackage1/__init__.py
# from <> import <>
# import <> is invalid !
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```

# Generator

`tupe(_ for _ in foo)`

# Pattern Matching
