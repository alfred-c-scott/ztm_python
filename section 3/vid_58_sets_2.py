my_set = {1, 2, 4, 5}
ur_set = {4, 5, 6, 7}
print(f'my_set:\t\t\t\t\t\t {my_set}')
print(f'ur_set:\t\t\t\t\t\t {ur_set}')
print(f'my_set.difference(ur_set):\t {my_set.difference(ur_set)}')
print(f'ur_set.difference(my_set):\t {ur_set.difference(my_set)}')

print()
set_0 = {1, 2, 3,}
print(f'set_0:\t\t\t\t\t\t {set_0}')
set_0.add(4)
print(f'set_0.add(\'4\'):\t\t\t\t {set_0}')
set_0.discard(4)
print()

set_1 = {3, 4, 5}
print(f'set_0:\t\t\t\t\t\t\t {set_0}')
print(f'set_1:\t\t\t\t\t\t\t {set_1}')
set_0.difference_update(set_1)
print(f'set_0.difference_update(set_1):\t {set_0}')
print()

set_a = {10, 11, 12, 13}
set_b = {12, 13, 14, 15}
print(f'set_a:\t\t\t\t\t\t\t {set_a}')
print(f'set_b:\t\t\t\t\t\t\t {set_b}')
print(f'set_a.intersection(set_b):\t\t {set_a.intersection(set_b)}')
print(set_a.intersection(set_b))
print()

set_x = {10, 11, 12, 13}
set_y = {12, 13, 14, 15}
set_z = {14, 15, 16, 17}
print(f'set_x:\t\t\t\t\t\t\t {set_x}')
print(f'set_y:\t\t\t\t\t\t\t {set_y}')
print(f'set_z:\t\t\t\t\t\t\t {set_z}')
print(f'set_x.union(set_y):\t\t\t\t {set_x.union(set_y)}')
print(f'set_x.union(set_z):\t\t\t\t {set_x.union(set_z)}')
print(f'set_x.isdisjoint(set_y):\t\t {set_x.isdisjoint(set_y)}')
print(f'set_y.isdisjoint(set_z):\t\t {set_x.isdisjoint(set_z)}')

set_i = {1, 2, 3}
set_j = {1, 2, 3, 4, 5, 6}
print(f'set_i:\t\t\t\t\t\t\t {set_i}')
print(f'set_j:\t\t\t\t\t\t\t {set_j}')
print(f'set_i.issubset(set_j):\t\t\t {set_i.issubset(set_j)}')
print(f'set_j.issubset(set_i):\t\t\t {set_j.issubset(set_i)}')
print(f'set_i.issuperset(set_j):\t\t {set_i.issuperset(set_j)}')
print(f'set_j.issuperset(set_i):\t\t {set_j.issuperset(set_i)}')
