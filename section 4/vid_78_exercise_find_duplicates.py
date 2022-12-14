# Exercise check for duplicates in the list and print the duplicates as a list

some_list = ['a', 'b', 'c', 'd', 'b', 'n', 'n']
some_list_copy = some_list

ctr_1 = 0
ctr_2 = 0

list_of_duplicates = []

# my solution
for x in some_list:
    ctr_1 += 1
    for y in some_list_copy:
        ctr_2 += 1
        if x == y and ctr_1 != ctr_2 and x not in list_of_duplicates:
            list_of_duplicates.append(x)
    ctr_2 = 0

print(str(list_of_duplicates) + '\n')

# instructor solution - instructor solution much cleaner
duplicates = []
for value in some_list:
    if some_list.count(value) > 1 and value not in duplicates:
        duplicates.append(value)

print(duplicates)