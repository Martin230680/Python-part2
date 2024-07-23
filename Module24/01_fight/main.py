import random


class Units:
    def __init__(self, name, id):
        self.health = 100
        self.unit_name = name
        self.id = id

    def print_units(self):
        print(self.unit_name, self.health)


unit1 = Units('Martin', 1)
unit2 = Units('Kapitan', 2)
while unit1.health > 0 and unit2.health > 0:
    hit = random.choice([unit1.id, unit2.id])
    if hit == unit1.id:
        print(f'удар пропустил {unit1.unit_name}')
        unit1.health -= 20
    else:
        print(f'удар пропустил {unit2.unit_name}')
        unit2.health -= 20
    unit1.print_units()
    unit2.print_units()
else:
    if unit1.health:
        print(f'Победу одержал - {unit1.unit_name}')
    else:
        print(f'Победу одержал - {unit2.unit_name}')