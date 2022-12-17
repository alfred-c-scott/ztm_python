a = 'hello'

if len(a) < 10:
    print(f'{a} is a perfect length of {len(a)}')

if (n := len(a)) < 10:
    print(f'{a} is a perfect length of {n}')

b = 'helloooooooooooooooooooo'

while (n := len(b)) > 1:
    print(n)
    b = b[:-1]

print(b)