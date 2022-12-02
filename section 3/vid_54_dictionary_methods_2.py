
user_0 = {
    'name': 'albert',
    'age': 44,
    'is_ok': True,
    'is_tired': False,
}

# prints True
print('name' in user_0)
# prints False
print('albert' in user_0)

# can be assigned to boolean variable
is_in = 'name' in user_0
print(is_in)
# prints False
print('albert' in user_0.keys())
# prints True
print('albert' in user_0.values())

# prints dictionary as tuples
print(user_0.items())
print('albert' in user_0.items())

# copies dictionary to user_1 then removes
# all key/value pairs from user_0
user_1 = user_0.copy()
user_0.clear()
print(user_0)
print(user_1)

# remove a key/value pair from a dictionary
popped_kv = user_1.pop('age')
print(popped_kv)
print(user_1)

# change the value in a key/value pair
user_1.update({'is_tired': True})
print(user_1['is_tired'])

# another way of adding a key/value pair
# to a dictionary
user_1.update({'age': 51})
print(user_1['age'])
print(user_1)
