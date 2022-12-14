# clean code
def is_even_0(num):
    if num % 2 == 0:
        return True
    else:
        return False

# removing the else statement is cleaner
def is_even_1(num):
    if num % 2 == 0:
        return True
    # won't execute if number is even
    return False

# even cleaner as a boolean is returned
def is_even_2(num):
    return num % 2 == 0
print('---------------------------------')
print(is_even_0(5))
print(is_even_0(4))
print('---------------------------------')
print('---------------------------------')
print(is_even_1(5))
print(is_even_1(4))
print('---------------------------------')
print('---------------------------------')
print(is_even_2(5))
print(is_even_2(4))
print('---------------------------------')
