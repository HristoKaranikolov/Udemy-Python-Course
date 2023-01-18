class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with {self.power}')


class Archer(User):
    def __init__(self, name, arrows_count):
        self.name = name
        self.arrows_count = arrows_count

    def attack(self):
        print(f'shooting with {self.arrows_count}')

    def check_arrows(self):
        print(f'{self.arrows_count} remaining')

    def run(self):
        print('ran fast')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


wizard = Wizard('Merlin', 100)
archer = Archer('Robin', 50)

wizard.sign_in()
archer.sign_in()

wizard.attack()
archer.attack()

hybrid1 = HybridBorg('Borgie', 90, 100)
print(hybrid1.name)
