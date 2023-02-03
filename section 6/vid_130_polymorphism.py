
class User:
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('do nothing')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f'attacking with Arrows: {self.num_arrows} left')

wizard_0 = Wizard('Merlin', 50)
archer_0 = Archer('Robin', 100)


wizard_0.attack()
archer_0.attack()

def player_attack(character):
    character.attack()

player_attack(archer_0)
player_attack(wizard_0)

for character in [wizard_0, archer_0]:
    character.attack()
