# error handling

def my_sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f'please enter numbers {err}')

print(my_sum(2, 4))

def my_sum2(num1, num2):
    try:
        return num1/num2
    except (TypeError, ZeroDivisionError):
        print('oops')

my_sum2('num1', 1)

my_sum2(3, 0)