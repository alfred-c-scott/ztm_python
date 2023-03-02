# square the list
my_list = [5, 4, 3]

print(list(map(lambda x: x * x, my_list)))

# sort the list
a = [(0, 2), (4, 3), (2, 9), (10, -1)]

a.sort(key=lambda x: x[1], reverse=True)

print(a)
