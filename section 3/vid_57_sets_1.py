# unordered collection of unique objects
my_set = {1, 2, 3, 4}
print(my_set)

# because 1 is already in the set this has
# effect
my_set.add(1)
print(my_set)

# because 7 is not already in the set this
# has no effect
my_set.add(7)
print(my_set)

set_to_list = list(my_set)
print(f'my_set:      {my_set}')
print(f'set_to_list: {set_to_list}')
my_list = [1, 2, 3, 4]

set(my_list)
list_to_set = set(my_list)

print(f'before conversion: {my_list}')
print(f'after conversion:  {list_to_set}')
