from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, length,width):
        super().__init__()
        self.__length = length
        self.__width=width
    
    def area(self):
        return 2#hier verder werken

class Square(Rectangle):
    def __init__(self, side):
        self.side = side

class Ellipse(Shape):
    def __init__(self,major_radius,minor_radius):
        super().__init__()
        self.__major_radius = major_radius
        self.__minor_radius=minor_radius
    
    def NotImplementedException(self):
        return False
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    