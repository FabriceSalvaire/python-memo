# update lags...
# refactor code -> errors at the wrong position
# box badly formated

####################################################################################################

# Ruff [I001]: Import block is un-sorted or un-formatted (eglot-check)
# Callable...# -> Callable..#
from collections.abc import Callable  # , Awaitable
from typing import NewType

UserId = NewType('UserId', int)


def use_callback(callback: Callable[[int, int], str]) -> None:
    ...

####################################################################################################

# Ruff [E261]: Insert at least two spaces before an inline comment
x = 1 # ...
x = 1  # ...
x = 1      # ...

# Ruff [E265]: Block comment should start with `# `
#! x = 2
