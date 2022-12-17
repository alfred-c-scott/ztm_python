# OOP
class PlayerCharacter:
    # constructor dunder method
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def run(self):
        print('run')

player_0 = PlayerCharacter('Stella', '12')
player_1 = PlayerCharacter('Sophia', age=9)

print(player_0)
print(player_0.name)

print(f'{player_0.name} is {player_0.age} years old')
print(f'{player_1.name} is {player_1.age} years old')

player_0.run()
player_1.run()
