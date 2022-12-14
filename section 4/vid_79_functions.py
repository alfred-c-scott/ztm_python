# functions help coding using the principle of DRY
print('-------------------------------')
def say_hello():
    print('hello')

say_hello()

print('-------------------------------')
print('-------------------------------')

image = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
 ]

def print_char(x):
    if x == 0:
        return ' '
    else:
        return '*'

def print_picture(x):
    for row in x:
        print (f'{print_char(row[0])}{print_char(row[1])}{print_char(row[2])}{print_char(row[3])}'
               f'{print_char(row[4])}{print_char(row[5])}{print_char(row[6])}')

print_picture(image)

print('-------------------------------')
print('-------------------------------')