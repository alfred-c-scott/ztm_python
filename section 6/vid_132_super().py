
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')



class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        self.num_arrows -= 1
        print(f'attacking with Arrows: {self.num_arrows} left')

wizard_0 = Wizard('Merlin', 50, 'wizard_0.email.com')
archer_0 = Archer('Robin', 100, 'archer_0.email.com')



print(wizard_0.email)
print(archer_0.email)
