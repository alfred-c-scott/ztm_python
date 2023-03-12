# higher order functions

# a function that takes another function as an argument
def greet(func):
    func()

# a function that returns another function
def greet2():
    def func():
        return 5
    return func

# map() filter() and reduce() are examples of higher order functions
