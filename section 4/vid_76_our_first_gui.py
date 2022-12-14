 # Exercise

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
 ]



# This is my solution, but it required using a function, and we have not gone over functions yet
def print_char(x):
    if x == 0:
        return ' '
    else:
        return '*'

for row in picture:
    print (f'{print_char(row[0])}{print_char(row[1])}{print_char(row[2])}{print_char(row[3])}'
           f'{print_char(row[4])}{print_char(row[5])}{print_char(row[6])}')

# this was the first idea I had but new it would end the print() function with a \n and knew it wouldn't work
"""
for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*')
        else:
            print(' ')
    print() # prints empty string ending with '\n' character
"""

print('\n\n')
# it turns out that there is a parameter, end=,  that can be added to the print function that we had not gone
# over yet that allows you to tell python to end the print statement with a character other than '.\n'
for image in picture:
    for pixel in image:
        if pixel == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
