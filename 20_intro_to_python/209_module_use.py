# Use of modules
import module_def
module_def.fib(1000)


import module_def as my_module
my_module.fib(1000)


from module_def import fib
fib(1000)


from module_def import *
fib(1000)
