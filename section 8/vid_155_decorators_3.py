# decorators

def decorator(func):
    def wrapper_func(*args, **kwargs):
        print('**************')
        func(*args, **kwargs)
        print('**************')
    return wrapper_func

@decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)

hello('testing')

