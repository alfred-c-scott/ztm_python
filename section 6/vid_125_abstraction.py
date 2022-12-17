# --------------------------------------------------------------------------
# a built-in example of abstraction is the len() function - we don't care
# about the code that checks the length of this list only that it returns
# the value
# --------------------------------------------------------------------------
my_list = [1, 2, 3, 4, 10, 15]
print(len(my_list))

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def run(self):
        print('run')
    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

    def return_self(self):
        return self

player_0 = PlayerCharacter('alfy', 44)
# calling the speak method on our instantiated player_0 is an example of
# abstraction because we don't care about the code that is being run we
# only care about the output
player_0.speak()


