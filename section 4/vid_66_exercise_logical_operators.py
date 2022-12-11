is_magician = True
is_expert = False

# check if magician and expert: 'you are a master magician'

# check if magician but not expert: 'at least you are getting there'

# if you are not a magician: 'you need magic powers'

# solution 1
print('-----------------------------------')
if is_magician and is_expert:
    print('you are a master magician')

elif is_magician:
    print('at least you are getting there')

else:
    print('you need magic powers')
print('-----------------------------------')
