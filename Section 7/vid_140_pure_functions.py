# example of a pure function
def multiply_by2(li):
    new_list_0 =[]
    for item in li:
        new_list_0.append(item*2)
    return new_list_0


print(multiply_by2([1, 2, 3]))

# when the function interacts with and changes values of objects outside
# the scope of the function like we see below, the function can no longer
# be called pure

new_list_1 = []

def multiply_by3(li):
    for item in li:
        new_list_1.append(item*3)
    return new_list_1

print(multiply_by3([1, 2, 3]))

