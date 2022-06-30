# Crear una clase que simule 
# el comportamiento de un punto en el plano cartesiano (x,y)
# Se debe poder mover el punto
# Se debe poder mover el punto a la psosicion incial (0,0)
# Se debe poder hallar la distancia entre dos puntos
from math import sqrt


class Point:
    def __init__(self,x, y) -> None:
        self.x = x
        self.y=y

    def reset(self):
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        x_1 = self.x
        y_1 = self.y

        x_2 = point.x
        y_2 = point.y

        resultado = sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
        return resultado

p1 = Point(5,2)
p2 = Point(4,6)

distance = p1.distance(p2)
print(distance)
p1.reset()
p2.reset()
p1.move(1,1)
distance = p1.distance(p2)
print(distance)