
import os

def function():
   retval = setattr(function, "bar", "baz")
   os.write(2, str(retval) + '\n')

def entry_point(argv):
    function()
    return 0

def target(*args):
    return entry_point, None
