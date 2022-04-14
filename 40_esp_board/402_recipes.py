""" Quick recipes """

# run a function myfn() from a file/module "test.py"
import test
test.myfn()


# Python3: reload the module after the file contents were changed
from importlib import reload
reload(test)

# uPython: reload the module after the file contents were changed
# uPython: soft reset
from machine import reset
reset()

# uPython: reload the module after the file contents were changed
# uPython: partial reset (does not work well with WebREPL)
Ctrl+C  # stops the current program
Ctrl+D  # performs a soft reset


# uPython: copy-paste program code into the terminal
Ctrl+E
<paste code>
Ctrl+D
