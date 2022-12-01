basket = [1, 2, 3, 4, 5]
# returns length of list
print(len(basket))
print(basket)

# add to end of list
basket.append(6)
print(basket)

# insert in list
basket.insert(4, 100)
print(basket)

new_list_0 = basket                 # copies list
new_list_1 = basket.insert(4, 101)  # updates but no copy made
print(new_list_0)
print(new_list_1)

basket.extend([102, 103])
print(basket)

basket.pop()
print(basket)

basket.pop()
print(basket)

basket.pop(0)
print(basket)

new_list_2 = basket.pop()   # returns value
print(new_list_2)

basket.remove(101)
print(basket)

new_list_4 = basket.remove(2)
print()
