class Auto:
    color = "Black"
    weight = 1500

    def __init__(self, brand="Jeep", age=3, mark="Renegade"):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(self.age)

auto_1 = Auto()
auto_1.move()
auto_1.stop()
auto_1.birthday()
