# public and private methods and variables in python
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def run(self):
        print('run')
    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')

    def return_self(self):
        return self

player_0 = PlayerCharacter('alfy', 1000)
player_0.speak()

# --------------------------------------------------------------------------
# because speak() method is public it can be altered by developers as
# seen when you run the following lines
# --------------------------------------------------------------------------
player_0.speak = 'boo'
print(player_0.speak)

# --------------------------------------------------------------------------
# python classes do not have the ability to make any of their variables or
# methods private - they can be overwritten and assigned new values by devs
# there are, however, conventions that communicate to other developers your
# intention to keep certain methods and variables private - See below
# --------------------------------------------------------------------------

class HockeyPlayer:

    # ----------------------------------------------------------------------
    # the underscore character is what is used to communicate to other devs
    # that a variable should be private
    # ----------------------------------------------------------------------
    def __init__(self, name, age, league, trophies):
        self._name = name
        self._age = age
        self.league = league
        self.trophies = trophies

    @staticmethod
    def _skate(self):
        print('now skating')