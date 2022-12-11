is_old = True
is_licensed = True

print('-----------------------------------')
if is_old and is_licensed:
    print(f'is_old = {is_old}')
    print(f'is_licensed = {is_licensed}')
    print('You can legally drive')
print('-----------------------------------')

is_old = 'hello'
is_licensed = 5

print('-----------------------------------')
if is_old and is_licensed:
    print('truthy values')
    print(f'is_old = {is_old}')
    print(f'is_licensed = {is_licensed}')
    print('You can legally drive')
print('-----------------------------------')

is_old = ''
is_licensed = 0
print('-----------------------------------')
print('falsey values')
if is_old and is_licensed:
    print(f'is_old = {is_old}')
    print(f'is_licensed = {is_licensed}')
    print('You can legally drive')
else:
    print(f'is_old = {is_old}')
    print(f'is_licensed = {is_licensed}')
    print('you can\'t legally drive')
print('-----------------------------------')