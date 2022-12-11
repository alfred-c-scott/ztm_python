is_old = True
is_licensed = True

print('-----------------------------------')
if is_old and is_licensed:
    print('is_old = True\nis_licensed = True')
    print('You can legally drive')
print('-----------------------------------')

is_tall = True
is_adult = False

# if rider is either tall or an adult they can ride
if is_tall or is_adult:
    print(f'is_tall = {is_tall}')
    print(f'is_adult = {is_adult}')
    print('you can ride the ride')
print('-----------------------------------')
