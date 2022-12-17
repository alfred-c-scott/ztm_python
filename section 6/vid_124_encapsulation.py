# encapsulation - an example of encapsulation would be the class
# we have been working on in previous videos. What you see is
# data and functionality encapsulated within a class
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

    def return_self(self):
        return self

player_0 = PlayerCharacter('alfy', 44)
player_0.speak()

# you can change the age or name
player_0.age = 43
player_0.name = 'alfred'
player_0.speak()
