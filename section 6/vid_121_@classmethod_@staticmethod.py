
class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things_0(cls, num1, num2):
        return num1 + num2

    @classmethod
    def adding_things_1(cls, num1, num2):
        return cls('anon', num1 + num2)

    @staticmethod
    def adding_things_2(num1, num2):
        return num1 + num2

player_0 = PlayerCharacter('Tom', 20)

print(player_0.shout())
print(player_0.adding_things_0(2, 3))

# class methods can be called without instantiating an object
print(PlayerCharacter.adding_things_0(2, 3))

# this would be a more common way of using a class method as it
# can access other class data
player_1 = PlayerCharacter.adding_things_1(3, 3)
print(player_1.name)

# the age is num1 + num 2
print(player_1.age)

# usage of static method
print(PlayerCharacter.adding_things_2(4,3))


