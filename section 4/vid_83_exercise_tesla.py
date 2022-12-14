age = int(input('What is your age: '))

def check_age(driver_age):
    if driver_age >= 16:
        return True
    else:
        return False

can_drive = check_age(age)

if can_drive:
    print('you can drive')
else:
    print('not old enough')
