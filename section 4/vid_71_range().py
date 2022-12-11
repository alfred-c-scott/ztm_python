print('------------------------')
print('for _ in range(0, 10):\n\tprint(_)')
print('------------------------')
# often when variable names aren't
# important an underscore is used
for _ in range(0, 10):
    print(_)

print('------------------------')
print('for _ in range(0, 10, 1):\n\tprint(_)')
print('------------------------')
# ranges accept a third parameter,
# the step over
for _ in range(0, 10, 1):
    print(_)

print('------------------------')
print('for _ in range(0, 10, 2):\n\tprint(_)')
print('------------------------')
for _ in range(0, 10, 2):
    print(_)

print('------------------------')
print('for _ in range(10, 0, -1):\n\tprint(_)')
print('------------------------')
# step over of -1 reverses order if
# range is set up in descending order
for _ in range(10, 0, -1):
    print(_)

print('------------------------')
print('for _ in range(10, 0, -2):\n\tprint(_)')
print('------------------------')
# step over of -2
for _ in range(10, 0, -2):
    print(_)

print('------------------------')
print('for _ in range(0, 10):\n\tprint(list(range(10)))')
print('------------------------')
for _ in range(0, 5):
    print(list(range(10)))

print('------------------------')
print('for _ in range(10):\n\tprint(list(range(10)))')
print('------------------------')
# output mirrors the print statements above
for _ in range(5):
    print(list(range(10)))
