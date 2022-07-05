import math
class Rectangle():

    def __init__(self, width:int=0, height:int=0) -> None:
        self.width = width
        self.height = height
        self.sides = 4
        
    def get_area(self) -> int:
        return int(self.width * self.height)

class Circle():
    def __init__(self, radius: str = int) -> None:
        self.radius = radius
        self.sides = 0
    
    def get_area(self):
        return self.radius * self.radius * math.pi


shapes = [Rectangle(6,10), Circle(7)]
print("Sides of a rectangle are ", str(shapes[0].sides))
print("Area of a rectangle are ", str(shapes[0].get_area()))


print("Sides of a circle are ", str(shapes[1].sides))
print("Area of a circle are ", str(shapes[1].get_area()))


class Shape:
    def __init__(self) -> None:
        self.sides = 0

    def get_area(self):
        return 8+2
    
    def otra_funcion(self):
        print("Esto hace algo genial")

class Rectangle(Shape):

    def __init__(self, width:int=0, height:int=0) -> None:
        self.width = width
        self.height = height
        self.sides = 4

    def get_area(self) -> int:
        return int(self.width * self.height)

class Circle(Shape):
    
    def __init__(self, radius: str = int) -> None:
        self.radius = radius
        self.sides = 0
    
    def get_area(self):
        return self.radius * self.radius * math.pi


print()
print()
print()
shapes = [Rectangle(6,10), Circle(7)]
print("Sides of a rectangle are ", str(shapes[0].sides))
print("Area of a rectangle are ", str(shapes[0].get_area()))
print("Otro of a rectangle are ", str(shapes[0].otra_funcion()))


print("Sides of a circle are ", str(shapes[1].sides))
print("Area of a circle are ", str(shapes[1].get_area()))
print("OTro of a circle are ", str(shapes[1].otra_funcion()))