# decorators


def my_decorator(func):
    def wrap_func():
        print('-----------------')
        func()
        print('-----------------')
    return wrap_func

@my_decorator
def hello():
    print('hello')

hello()

@my_decorator
def bye():
    print('bye')

bye()
