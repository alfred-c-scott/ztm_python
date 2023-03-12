# practical application of decorators
from time import time

# this decorator will print to terminal the time (in seconds) the decorated function takes to complete
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()
