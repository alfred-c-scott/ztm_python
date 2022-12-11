# counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('------------------------')
ct = 0
total = 0
# my solution
for num in my_list:
    if ct == 0:
        total = num
        ct += 1
    else:
        total = total + num
print(total)

print('------------------------')
print('------------------------')
# instructor solution
counter = 0
for num in my_list:
    counter = counter + num
print(total)
print('------------------------')
