# dictionaries are sets of unordered key/value pairs
context_0 = {
    'a': 1,
    'b': 2,
    'c': 3
}

print(context_0['a'])

# print(context['z']) returns error because key is
# not in dictionary

my_list = [
    {'a': 1,
     'b': 2,
     'c': 3},
    {'x': [1, 2, 3],
     'y': 5,
     'z': 'a'}
]
print(my_list[0])
print(my_list[1])
print(my_list[0]['a'])
print(my_list[1]['x'])
list_in_dict = my_list[1]['x']
print(list_in_dict[0])
