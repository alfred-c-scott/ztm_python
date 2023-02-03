# always be testing out new features as you are learning them
# for example here I added a function that will return self
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def return_self(self):
        return self

player_0 = PlayerCharacter('Stella', 12)
print(player_0.return_self())
