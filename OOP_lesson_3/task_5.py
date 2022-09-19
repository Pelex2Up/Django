class Robot:
    my_robots = dict()

    def __init__(self, name):
        self.name = name
        self.weapon = input('Выберите оружие для робота (меч/автомат): ').lower()
        if self.weapon == 'меч':
            self.damage = 10
        else:
            self.damage = 40
        self.armor = input('Выберите броню для робота (нагрудник/шлем): ').lower()
        if self.armor == 'шлем':
            self.strength = 80
        else:
            self.strength = 100
        self.my_robots.update({self.name: [[f"Оружие: {self.weapon}", f"Урон: {self.damage}"],
                                                  [f"Броня: {self.armor}", f'Прочность: {self.strength}']]})

    def show_info(self):
        return print(f'Робот {self.name}. Его снаряжение: {self.weapon}-{self.damage} урона, {self.armor}-{self.strength} прочности')


robot1 = Robot('Savage')
robot1.show_info()
