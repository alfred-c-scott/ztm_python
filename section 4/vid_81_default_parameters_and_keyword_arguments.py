# parameters
def say_hello_0(name, emoji):
    print(f'hello {name} {emoji}')

#default arguments
def say_hello_1(name='Default', emoji=':('):
    print(f'hello {name} {emoji}')

# positional arguments
say_hello_0('Alfred', ':-)')

# keyword arguments
say_hello_0(name='Bibi', emoji=':)')

# if arguments not passed to function the default will be used
say_hello_1()
say_hello_1('rocket_man')
