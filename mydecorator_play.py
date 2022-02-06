
def asterix(func):
    def func_wrapper(x):
        print("*"*len(x))
        func(x)
        print("*"*len(x))
    return func_wrapper

@asterix
def capitalize(x):
    print(x.upper())

capitalize("I am here!",55)