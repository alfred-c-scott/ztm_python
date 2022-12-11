is_old = True
is_licensed = True

print('-----------------------------------')
if is_old:
    print('is_old = True')

# set to false before next loop
is_old = False

if is_old:
    print('is_old = True')
else:
    print('is_old = False')
print('-----------------------------------')

is_old = True
if is_old and is_licensed:
    print('is_old = True\nis_licensed = True')
    print('You can legally drive')
print('-----------------------------------')

is_tall = True
is_adult = False

if is_tall or is_adult:
    print('you can ride the ride')
