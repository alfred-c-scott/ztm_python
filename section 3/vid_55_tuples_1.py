# tuple - immutable list
# not as flexible as a list however because they
# can't be changed there is less ambiguity to for
# another coder if they look at your code they are
# also a lot faster to than lists

tuple_0 = (1, 2, 3, 4, 5, 6, 7)
print(tuple_0)
print(len(tuple_0))

if 5 in tuple_0:
    # prints 6th item in tuple
    print(tuple_0[5])

# because tuples are immutable they can be used as
# a key in a dictionary

my_dictionary = {
    'a': ['a', 'b', 'c'],
    (0, 1): ['e', 'f', 'g'],
}

print(my_dictionary['a'][0])
print(my_dictionary[(0, 1)][0])
