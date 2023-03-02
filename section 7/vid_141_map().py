# map, filter, zip, and reduce
list_0 = [1, 2, 3, 4]
list_1 = ['lifer', 'by', 'nature']

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, list_0)))

def replace_item(li):
    for i in range(len(li)):
        li[i] = li[i].capitalize()

replace_item(list_1)

print(list_1)

