# file i/o

with open('data_file', mode='r') as my_file_0:
    print(my_file_0.readlines())

# appends to the end of the file
with open('data_file', mode='a') as my_file_1:
    text = my_file_1.write('\nhey it\'s me')
    print(text)

# will not create a file that doesn't already exist with the r+ mode
with open('data_file_2', mode='w') as my_file_2:
    text = my_file_2.write('hey it\'s me')
    print(text)