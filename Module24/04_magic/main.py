class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

class Air:
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Shtorm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

class Water:
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Shtorm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return None

class Earth:
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None

class Shtorm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Dirt:
    name = 'Грязь'


class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()


magic = water + air
print(f'Вода + Воздух = {magic.name}')

magic = water + fire
print(f'Вода + Огонь = {magic.name}')

magic = water + earth
print(f'Вода + Земля = {magic.name}')

magic = air + fire
print(f'Воздух + Огонь = {magic.name}')

magic = air + earth
print(f'Воздух + Земля = {magic.name}')

magic = fire + earth
print(f'Огонь + Земля = {magic.name}')

