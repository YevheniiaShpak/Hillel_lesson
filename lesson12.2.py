import time

class Auto:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(self.age)

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")

truck1 = Truck(brand="Volvo", age=5, mark="TruckMark1", max_load=7000)
truck1.move()
truck1.load()
print(f"Max load of {truck1.brand}: {truck1.max_load} kg")
print("____"*10)
car2 = Car(brand="Ford", age=1, mark="CarMark2", max_speed=200)
car2.move()
print(f"Max speed of {car2.brand}: {car2.max_speed} km/h")




