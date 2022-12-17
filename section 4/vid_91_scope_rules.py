# scope rules
# 1 - start with local
# 2 - parent local
# 3 - global
# 4 - built in python
print('------------------------------------')
a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

print('------------------------------------')
print('------------------------------------')

b = 1
# parent local example
def parent():
    b = 10
    def some_function():
        return b
    return some_function()

print(b)
print(parent())

print('------------------------------------')
print('------------------------------------')

c = 1
# global example

def rocket_function():
    c = 4
    print(c)

print(c)
rocket_function()

print('------------------------------------')
