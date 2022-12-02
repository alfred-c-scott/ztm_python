context_dict = {
    'basket': [1, 2, 3],
    'greeting': 'hello',
}

print(context_dict['basket'])

# returns None
print(context_dict.get('book'))

user_0 = {
    'name': 'albert',
    'age': 44,
    'is_ok': True,
    'is_tired': False,
}

print(user_0.get('name'))

# returns None
print(user_0.get('fav_color'))

# prints green as default value but the value is not
# stored in the dictionary
print(user_0.get('fav_color', 'green'))

# prints None as the previous action did not store
# "green" in the dictionary
print(user_0.get('fav_color'))

# adds 'fav_color' key with value 'green'
user_0['fav_color'] = 'green'
# since 'fav_color' is now in dictionary it will print
print(user_0.get('fav_color'))

# alternate way to declare a dictionary
user_1 = dict(name='JohnJohn')
print(user_1['name'])
