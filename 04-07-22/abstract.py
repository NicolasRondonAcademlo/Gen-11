from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass


    @abstractmethod
    def get_area(self, *args, **kwargs):
        pass

    @abstractmethod
    def turn_rgb(self):
        pass


class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def get_area(self, *args, **kwargs):
        return  self.width * self.height

    def turn_rgb(self):
        return "Se encendio el rgb del rectangulo"


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    
    def get_area(self, *args, **kwargs):
        return  (self.base * self.height) // 2

    def turn_rgb(self):
        return "Se encendio el rgb del triangulo"




fig_1 = Rectangle(8,4)
fig_2 = Triangle(8,4)

def say_area_turn_rgb(obj_shape):
    area = obj_shape.get_area()
    rgb = obj_shape.turn_rgb()
    return [area,rgb]

b = say_area_turn_rgb(fig_2)
print(b)
