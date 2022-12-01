basket_0 = ['a', 'c', 'r', 'n', 'r', 'z']
print(f'original list:\t\t {basket_0}')
basket_0.sort()
print(f'basket_0.sort():\t {basket_0}')
basket_0.reverse()
print(f'basket_0.reverse():\t {basket_0}')
# reverses basket again using slice
print(f'basket_0[::-1]:\t\t {basket_0[::-1]}')
# unlike .sort() this creates copy in memory
# with the original preserved in memory
print(f'basket_0:\t\t\t {basket_0}')
print('\n\n')

# range
list_0 = list(range(1, 10))
print(f'list_0 = list(range(1, 20)):\t {list_0}')

sentence = ' '
new_sentence_0 = sentence.join(['hi', 'my', 'name', 'is', 'alfred'])
print(sentence)
print(new_sentence_0)

# the previous actions in one line
new_sentence_1 = ' '.join(['hi', 'my', 'name', 'is', 'alfred'])
print(new_sentence_1)
