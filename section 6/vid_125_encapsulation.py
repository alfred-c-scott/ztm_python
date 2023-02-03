class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')

player_0 = PlayerCharacter('Ryan', 450)

player_0.run()
player_0.speak()
