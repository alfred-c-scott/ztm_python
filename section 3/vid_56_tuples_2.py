tuple_0 = (1, 2, 3, 4, 4, 4,)
tuple_1 = tuple_0[1:2]

print(tuple_0)
print(tuple_1)

print(tuple_0[0])

a, b, c, d, e, f, g, h, = (1, 2, 3, 4, 5, 6, 7, 8,)
i, j, k, *other, l, = (1, 2, 3, 4, 5, 6, 7, 8,)

print(i)
print(j)
print(k)
print(l)
print(other)

# .count method returns number of times argument
# appears in tuple
print(tuple_0.count(4))

print(tuple_0.index(3))
