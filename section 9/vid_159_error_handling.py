# error handling

age0 = input('what is your age?')
print(age0)

# the user can input any string and the program will run however only integers make sense.
# so we need a way to handle these errors

# wrapping the input inside an int throws an error
age1 = int(input('what is your age?'))
print(age1)

# the following code works at catching an error but will stay in this loop forever
while True:
    try:
        age2 = int(input('what is your age?'))
        print(age2)
    except:
        print('please enter an integer')
    # adding an else statement after except is the same as an if statement and will prevent this from looping
    # forever after good input is entered by user
    else:
        print('thank you!')
        break

while True:
    try:
        age3 = int(input('what is your age? '))
        x = 10/age3
    # handles non integer entries
    except ValueError:
        print('please enter an integer')
    # handles divide by zero error
    except ZeroDivisionError:
        print('Enter non-zero age: ')
    # adding an else statement after except is the same as an if statement and will prevent this from looping
    # forever after good input is entered by user
    else:
        print('thank you!')
        break
