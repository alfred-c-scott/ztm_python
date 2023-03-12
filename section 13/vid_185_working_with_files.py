#!/usr/bin/python3
# file i/o

my_file = open('data_file')
print(my_file.read())

# nothing will be printed here because the cursor is in the wrong place after reading the file
print(my_file.read())

# to read the file again the cursor needs to be at the beginning of file and this can be
# accomplished using the seek method as seen below
my_file.seek(0)
print(my_file.read())

my_file.seek(0)
# reads the first line
print(my_file.readline())
# reads the second line
print(my_file.readline())

my_file.seek(0)
print(my_file.readlines())

my_file.close()
