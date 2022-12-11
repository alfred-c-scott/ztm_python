"""

iterable - a collection of items like list, dictionary, tuple, string, set
iterate  - one by one check each item in the collection

"""

users = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

print('------------------------')
# prints keys
for item in users:
    print(item)

print('------------------------')
print('------------------------')
# prints a tuple
for item in users.items():
    print(item)

print('------------------------')
print('------------------------')
# prints a formatted key and value
for item in users.items():
    key, value = item
    print(f'key = {key}, value = {value}')

print('------------------------')
print('------------------------')
# another way to print a formatted key and value
for k, v in users.items():
    print(f'key = {k} value = {v}')

print('------------------------')
print('------------------------')
# prints values in dictionary
for item in users.values():
    print(item)

print('------------------------')
print('------------------------')
# prints keys in dictionary
for item in users.keys():
    print(item)

print('------------------------')
print('------------------------')
# strings are iterable so this will work
my_str = 'test_string'
for char in my_str:
    print(char)
