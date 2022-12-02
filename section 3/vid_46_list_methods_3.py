basket_0 = ['a', 'b', 'c', 'd', 'e', 'a']

# prints None
print(basket_0.sort())

# modifies basket_0 in memory
basket_0.sort()
print(basket_0)

basket_1 = ['a', 'b', 'c', 'd', 'e', 'a']
print(basket_1)

# creates a copy of basket_1 sorted but
# basket_1 remains unchanged in memory
print(sorted(basket_1))
print(basket_1)

# reverses order of items in basket_1
basket_1.reverse()
print(basket_1)

# returns None
new_basket = basket_1.reverse()
print(new_basket)
