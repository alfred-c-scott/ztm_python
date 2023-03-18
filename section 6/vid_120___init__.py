class PlayerCharacter0:
    # class object attribute
    membership = True

    def __init__(self, name='anon', age=18):
        if age >= 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

player_0 = PlayerCharacter0('Stella', 18)
player_1 = PlayerCharacter0()
print(player_0.name)
print(player_1.name)
print(player_0.shout())
print(player_1.shout())