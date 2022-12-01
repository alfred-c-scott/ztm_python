context_dict = {
    123: [1, 2, 3],
    True: 'hello',
}

# keys must be immutable the following will print without error
print(context_dict[123])
print(context_dict[True])
