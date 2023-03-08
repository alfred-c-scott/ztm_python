# quick way to create lists, sets, and dictionaries

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# using comprehensions

# list comprehensions
my_li = [char for char in 'iterable']
print(my_li)

my_li2 = [num for num in range(0, 100)]
print(my_li2)

my_li3 = [num*2 for num in range(0, 100)]
print(my_li3)

my_li4 = [num**2 for num in range(0, 100) if num%2 == 0]
print(my_li4)


# set comprehensions
my_set1 = {char for char in 'iterable'}
print(my_set1)

my_set2 = {num for num in range(0, 100)}
print(my_set2)

my_set3 = {num*2 for num in range(0, 100)}
print(my_set3)

my_set4 = {num**2 for num in range(0, 100) if num%2 == 0}
print(my_set4)

# dictionary comprehensions
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict1 = {key:value**2 for key, value in simple_dict.items()}

print(my_dict1)

my_dict2 = {k:k*2 for k in [1, 2, 3]}

print(my_dict2)
