amazon_cart = [
    'notebooks',
    'pencils',
    'pens',
    'erasers',
]

new_cart_0 = amazon_cart        # updates amazon_cart in memory
new_cart_1 = amazon_cart[:]     # creates a copy in separate memory address
new_cart_0[0] = 'gum'
print(f'new cart_0:  {new_cart_0}')
print(f'new_cart_1:  {new_cart_1}')
print(f'amz_cart:  {amazon_cart}')
