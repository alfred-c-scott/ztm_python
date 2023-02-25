# introspection - the ability to determine the type of object at runtime

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

wizard_0 = Wizard('Merlin', 60, 'mern@email.com')

# tells you what methods and variables wizard_0 has access to.
print(dir(wizard_0))