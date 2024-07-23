# TODO здесь писать код
class Property():
    def __init__(self, worth):
        self.worth = worth

    def nalog(self):
        pass


class Apartment(Property):
    # def __init__(self, worth):
    #     super().__init__(worth)

    def nalog(self):
        return round(self.worth / 1000, 2)


class Car(Property):
    # def __init__(self, worth):
    #     super().__init__(worth)

    def nalog(self):
        return round(self.worth / 200, 2)


class CountryHouse(Property):
    # def __init__(self, worth):
    #     super().__init__(worth)

    def nalog(self):
        return round(self.worth / 500, 2)


total_money = int(input('Введите количество имеющихся денег: '))
print('Введите стоимость имущества: ')

wroth_apart = float(input('Стоимость квартиры ?  : '))
apart = Apartment(wroth_apart)
nalog_apart = apart.nalog()
print('Налог на квартиру {}'.format(nalog_apart))

wroth_car = float(input('Стоимость машины ? : '))
car = Car(wroth_car)
nalog_car = car.nalog()
print('Налог на машину {}'.format(nalog_car))

wroth_dacha = float(input('Стоимость дачи ? : '))
dacha = CountryHouse(wroth_dacha)
nalog_dacha = dacha.nalog()
print('Налог на дачу {}'.format(nalog_dacha))

sum_nalog = nalog_apart + nalog_car + nalog_dacha
result = sum_nalog - total_money
if result > 0:
    print('Денег на уплату налогов не хватает, в размере {} рублей'.format(round(result, 2)))
else:
    print('Всего налога на сумму {}, денег хватает'.format(sum_nalog))
