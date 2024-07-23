import math


class MyMath:
    @classmethod
    def circle_circumference(cls, radius: float) -> float:
        """Вычисление длины окружности."""
        return 2 * math.pi * radius

    @classmethod
    def circle_area(cls, radius: float) -> float:
        """Вычисление площади окружности."""
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, side_length: float) -> float:
        """Вычисление объёма куба."""
        return side_length ** 3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        """Вычисление площади поверхности сферы."""
        return 4 * math.pi * radius ** 2


radius = 5
side_length = 3

print("Длина окружности с радиусом", radius, ":", MyMath.circle_circumference(radius))
print("Площадь окружности с радиусом", radius, ":", MyMath.circle_area(radius))
print("Объём куба со стороной", side_length, ":", MyMath.cube_volume(side_length))
print("Площадь поверхности сферы с радиусом", radius, ":", MyMath.sphere_surface_area(radius))
