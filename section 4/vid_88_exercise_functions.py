# create a function called highest_even() that takes a list of integers as a parameter and returns
# the biggest integer that divides by 2 without a remainder


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 19, 15]
# my solution
def highest_even_0(num_list):
    numbers_list.sort()
    # print(numbers_list)
    numbers_list.reverse()
    # print(numbers_list)
    for num in numbers_list:
        if num % 2 == 0:
            return num
    return False

print(highest_even_0(numbers_list))

#instructor solution
def highest_even_1(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)

print(highest_even_1(numbers_list))
