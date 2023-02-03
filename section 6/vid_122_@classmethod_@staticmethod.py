class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player_1 = PlayerCharacter('Alf', 44)

print(player_1.adding_things(5, 5))

# @classmethod allows us to use the classes member function without
# instantiating the class
print(PlayerCharacter.adding_things(5, 5))

# similar to @classmethod with the difference being that @staticmethod
# does not have access to the class
print(PlayerCharacter.adding_things2(5, 5))

