print('---------------------------------------------')
for item in [1, 2, 3]:
    print(item)
print('---------------------------------------------')
print('---------------------------------------------')
i = 0
my_list = [1, 2, 3]
while i < len(my_list):
    print(i, my_list[i])
    i += 1

print('---------------------------------------------')
print('---------------------------------------------')
# the most common way to use a while loop is with
# while True: condition
while True:
    response = input('say something: ')
    if response == 'bye':
        break
