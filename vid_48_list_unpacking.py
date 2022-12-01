a, b, c, *other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(other)

d, e, f, *other, g =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d)
print(e)
print(f)
print(other)
print(g)

print('\n')
for i in other:
    print(i)
