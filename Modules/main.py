# import numpy


def reveal_params(func):
    print( locals())
    print(func.__code__.co_varnames)


@reveal_params
def foo(string="hello"):
    return string


print(foo("ki"))
