# OOP
class PlayerCharacter:
    # class object attribute is a static attribute
    membership = True
    # constructor dunder method
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def run(self):
        print('run')

player_0 = PlayerCharacter('Stella', 12)
player_1 = PlayerCharacter('Sophia', 9)
# checking if order matters
player_2 = PlayerCharacter(12, 'Coop')
print(f'{player_2.name} is {player_2.age} years old')

player_3 = PlayerCharacter(name='Mama Brooke', age=25)
print(f'{player_3.name} is {player_3.age} years old')

print(player_0.membership)


class PlayerCharacterEx2:
    # class object attribute is a static attribute
    membership = True
    # constructor dunder method
    def __init__(self, name, age):
        if self.membership is True:
            self.name =  name
            self.age = age

    def run(self):
        print('run')

    def shout(self):
        print(f'my name is {self.name}')

player_4 = PlayerCharacterEx2('Lynne', 65)

print(f'{player_4.name} is {player_4.age} years old')

player_4.shout()