""" Quick recipes """

# run a function myfn() from a file/module "test.py"
import test
test.myfn()


# Python3: reload the module after the file contents were changed
from importlib import reload
reload(test)


# uPython: reload the module after the file contents were changed
from machine import reset
reset()
# wait for the prompt and then
import test
test.myfn()


# uPython: soft reset
from machine import reset
reset()

