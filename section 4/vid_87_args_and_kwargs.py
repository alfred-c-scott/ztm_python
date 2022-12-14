# *args **kwargs
print('---------------------------------')
def super_function_0(*args):
    print(args)
    print(*args)
    return sum(args)

summed_num_0 = super_function_0(1, 2, 3)

print(summed_num_0)
print('---------------------------------')
print('---------------------------------')
def super_function_1(**kwargs):
    total = 0
    # prints a dictionary
    print(kwargs)
    for items in kwargs.values():
        total += items
    return total

summed_num_1 = super_function_1(n0 = 1, n1 = 2, n2 = 3)

print(summed_num_1)
print('---------------------------------')
print('---------------------------------')

def super_function_2(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

summed_num_2 = super_function_2(1, 2, 3, n0=1, n1=2, n3=3)

print(summed_num_2)
print('---------------------------------')
print('---------------------------------')

# rule: the order matters when building your functions - (params, *args, default params, **kwargs)
# example below

def test_func(name, *args, i='hi', **kwargs):
    kwarg_total = 0
    print(name)
    print(i)
    arg_total = (sum(args))
    for items in kwargs.values():
        kwarg_total += items
    string_to_return = f'{i} {name} the total is {arg_total + kwarg_total}'
    return string_to_return
    # return total

print(test_func('alfred', 1, 2, 3, i='hello', n1=1, n2=2, n3=3))
print('---------------------------------')