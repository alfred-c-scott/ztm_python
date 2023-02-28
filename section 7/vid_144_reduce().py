from functools import reduce

list_0 = [1, 3, 4]
list_1 = [2, 4, 6]
list_2 = [5, 4, 3]

def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, list_0, 0))
print(list_0)
