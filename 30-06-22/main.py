
class ParentClass:
    pass


# Diamond problem oop

class ChildClass(ParentClass ):
    pass


class Vehicle:
    def __init__(self, make, color, model) -> None:
        self.make = make
        self.color = color
        self.model = model

    def print_details(self):
        return {
            "Manufacter": self.make,
            "Color": self.color,
            "Model": self.model
        }
    

class Car(Vehicle):
    def __init__(self, make, color, model, doors) -> None:
        self.doors = doors
        super().__init__(make, color, model)


    def print_car_details(self):
        print(self.print_details())
        print("Doors", self.doors)
        return 


obj1 = Car("Susuki", "grey", "2015", 4)
obj1.print_car_details()


# Single
# Multi - Level
# Hierarchical
# Multiple
# Hibrida

class Vehicle:
    def set_to_speed(self, speed):
        self.speed = speed
        print("Speed iis set to", self.speed)


class Car(Vehicle):
    def open_trunk(self):
        print("Trunk is open")

class Motorcycle(Vehicle):
    def do_horse(self):
        print("Doing Horse")


corolla = Car()
corolla.set_to_speed(55)
corolla.open_trunk()


suzuki = Motorcycle()
suzuki.do_horse()
suzuki.set_to_speed(100)

import math
# Multilevel

class Vehicle:
    def set_to_speed(self, speed):
        self.speed = speed
        print("Speed iis set to", self.speed)

class Car(Vehicle):
    def open_trunk(self):
        print("Trunk is open")


class Hybrid(Car):
    def turn_hybrid(self):
        print("Hybrid mode is on")

print("-------")
prius_prime = Hybrid()
prius_prime.set_to_speed(220)
prius_prime.open_trunk()
prius_prime.turn_hybrid()