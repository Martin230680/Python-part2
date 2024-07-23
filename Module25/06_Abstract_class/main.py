from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, bottom, height):
        self.bottom = bottom
        self.height = height

    def area(self):
        return self.bottom * self.height * 0.5


circle = Circle(10)
rectangle = Rectangle(4, 6)
triangle = Triangle(3,8)

circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

print("Площадь круга:", round(circle_area, 2))
print("Площадь прямоугольника:",  round(rectangle_area, 2))
print("Площадь треугольника:",  round(triangle_area, 2))
