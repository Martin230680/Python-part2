import random


class House:
    food = 50
    money = 0


class Human:

    def __init__(self, name):
        self.name = name
        self.sitosti = 50

    def eat(self):
        self.sitosti += 1
        House.food -= 1
        string = f'ест, его сытость {self.sitosti} остатки еды в доме: {House.food}'
        return string

    def work(self):
        self.sitosti -= 1
        House.money += 1
        string = f'пошел на работу, сытость стала: {self.sitosti} денег в доме прибавилось: {House.money}'
        return string

    def play(self):
        self.sitosti -= 1
        string = f'стал играеть, сытость стала: {self.sitosti}'
        return string

    def go_to_market(self):
        House.food += 1
        House.money -= 1
        string = f'идет в магазин, еда {House.food} деньги {House.money}'
        return string


man1 = Human('Иван')
man2 = Human('Петро')

for i_day in range(365):
    number_dice = random.randint(1, 6)
    random_man = random.choice([man1, man2])
    if random_man.sitosti < 0:
        print(f'К сожалению, {random_man.name} помер с голоду ')
        break
    if random_man.sitosti < 20 and House.food >= 10:
        string = random_man.eat()
    elif House.food < 10:
        string = random_man.go_to_market()
    elif House.money < 50:
        string = random_man.work()
    elif number_dice == 1:
        string = random_man.work()
    elif number_dice == 2:
        string = random_man.eat()
    else:
        string = random_man.play()
    print(random_man.name, string)
if i_day == 364:
    print('прошел год, все живы!')
else:
    print('печалька')