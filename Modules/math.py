# !TODO: TO FIX THIS


def debugger(function):
    def print_locals():
        function()
        print(locals())

    return print_locals()


@debugger
def foo():
    x = 2


foo()


def func(func_):
    def return_locals():
        x = "hello world"
        func_()
        print(locals())

    return return_locals()


@func
def foo():
    return "hello world"


func(foo)
