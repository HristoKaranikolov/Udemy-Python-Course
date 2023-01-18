class PlayerCharacter:
    # Class object attribute
    membership = True

    def __init__(self, name='anonymous', age=0):
        if age > 18:
            self.name = name  # instance attribute
            self.age = age
        else:
            print('Player is not old enough!')

    def run(self):
        print('run')
        return 'done'

    def shout(self):
        print(f"My name is {self.name}!")

    @classmethod
    def adding_things(cls, name, num1, num2):
        return cls(name, num1 + num2)

    @staticmethod
    def adding(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Ichigo', 21)
player2 = PlayerCharacter('Neliel', 20)
player3 = PlayerCharacter()
player4 = PlayerCharacter.adding_things('anonymous', 2, 3) # This player has no access to the class methods
# because it is not instantiated inside the __init_ method, but added with the class method.

print(player1.name)
print(player1.age)
print(player2.name)
player1.run()
player2.shout()
# print(player4.shout()) This will not work
# player3.name - This will not be able to work,
# because the player default age is below 18.
