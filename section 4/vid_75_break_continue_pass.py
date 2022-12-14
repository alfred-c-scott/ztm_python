my_list = [1, 2, 3,]

for item in my_list:
    print(item)
    continue

for item in my_list:
    # stubbed while I am thinking about what to do with this function
    pass

for item in my_list:
    if len(my_list) == 3:
        print('is length of three')
        break
    else:
        print('length is not three')

# none of the examples in the tutorial made any real use of continue,
# so I found this on stackoverflow
#
# https://stackoverflow.com/questions/38513718/is-the-continue-statement-necessary-in-a-while-loop
"""
When  you run this, you won't see dog printed. That's because when python sees continue, it skips the 
rest of the while suite and starts over from the top.

You won't see 'horse' or 'cow' either because when 'horse' is seen, we encounter the break which exits 
the while suite entirely.
"""
animals = ['dog', 'cat', 'pig', 'horse', 'cow']
while animals:
    a = animals.pop()
    if a == 'dog':
        continue
    elif a == 'horse':
        break
    print(a)

