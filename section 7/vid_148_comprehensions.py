# quick way to create lists, sets, and dictionaries

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# using comprehensions

my_li =[char for char in 'iterable']

print(my_li)

my_li2 = [num for num in range(0, 100)]
print(my_li2)

my_li3 = [num*2 for num in range(0, 100)]
print(my_li3)

my_li4 = [num**2 for num in range(0, 100) if num%2 == 0]
print(my_li4)
