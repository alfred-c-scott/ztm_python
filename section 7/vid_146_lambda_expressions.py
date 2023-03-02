# lambda functions are anonymous functions are used only once
from functools import reduce

my_list = [1, 2, 3]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item%2 !=0

print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 !=0, my_list)))

print(my_list)
