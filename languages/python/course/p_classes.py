# A class is a blueprint for objects (instances).
# Methods are functions inside the class; properties live on self.
# __init__ runs when you create (instantiate) the object.

class Car:
    # Class property shared by all Car instances.
    brand = ["Volvo", "Tesla"]

car1 = Car()
print(car1.brand[0])
car2 = Car()
print(car2.brand[1])

class Vehicle:
    def __init__(self, brand, doors=4, wheels=4):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_greeting(self):
        print(
            "Hi, I'm your new car. My name is " + self.brand +
            " and I have " + str(self.doors) + " doors, and " +
            str(self.wheels) + " wheels!"
        )

vehicle1 = Vehicle("Volvo", 5, 5)
print(vehicle1.brand, vehicle1.doors, vehicle1.wheels)
vehicle1.car_greeting()

vehicle2 = Vehicle("VW")
print(vehicle2.brand)
