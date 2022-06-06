#!/usr/bin/env python3


def another_function(func):

    def other_func():
        val = "Результат от %s это %s" % (func(), eval(func()))
        return val
    
    return other_func
 
 
@another_function
def a_function():
    return "1+1"
 
value = a_function()
print(value)
