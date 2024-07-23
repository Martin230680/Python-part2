from random import randint, choice


class KillError(Exception):
    def __str__(self):
        return 'KillError'


class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(Exception):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'


class Karma:
    def __init__(self):
        self.karma_count = 0
        self.days_count = 0
        self.exepts_tuple = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]

    def one_day(self):
        self.days_count += 1
        try:
            if randint(1, 10) == 1:
                raise choice(self.exepts_tuple)
            else:
                self.karma_count += randint(1, 7)
        except Exception as exc:
            with open('karma.log', 'a', encoding='UTF-8') as file:
                file.writelines(f'\nДень {self.days_count}, ошибка: {exc}')


p = Karma()
while p.karma_count < 500:
    p.one_day()
print(f'День {p.days_count}, набрано {p.karma_count}  очков кармы.')
