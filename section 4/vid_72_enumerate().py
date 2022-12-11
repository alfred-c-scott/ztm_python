print('---------------------------------------------')
print('for i, char in enumerate(\'h0000-yaaaaa\'):\n\tprint(i, char)')
print('---------------------------------------------')
for i, char in enumerate('h0000-yaaaaa'):
    print(i, char)

print('---------------------------------------------')
print('my_list = [\'a\', \'b\', \'c\', \'d\', \'e\', \'f\']')
print('for i, char in enumerate(my_list):\n\tprint(i, char)')
print('---------------------------------------------')
my_list = ['a', 'b', 'c', 'd', 'e', 'f']
for i, char in enumerate(my_list):
    print(i, char)

print('---------------------------------------------')
print('my_tuple = (\'a\', \'b\', \'c\', \'d\', \'e\', \'f\')')
print('for i, char in enumerate(my_tuple):\n\tprint(i, char)')
print('---------------------------------------------')
my_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
for i, char in enumerate(my_tuple):
    print(i, char)
print('---------------------------------------------')
print('for i, char in enumerate(list(range(100))):\n\tif char == 50:\n\t\tprint(f\'the index of the number 50 is {i}\')')
print('---------------------------------------------')
for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'the index of the number 50 is {i}')

print('---------------------------------------------')
