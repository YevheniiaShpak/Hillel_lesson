import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"Circle(Radius: {self.radius}, Center: {super().__str__()})"

    def __eq__(self, other):
        return self.radius == other.radius

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        radius = math.fabs(self.radius - other.radius)
        center = Point(self.x - other.x, self.y - other.y)
        return Circle(radius, center) if radius > 0 else Point(center.x, center.y)

circle1 = Circle(radius=5, x=7, y=0)
circle2 = Circle(radius=5, x=2, y=2)
result = circle1 == circle2
result1 = circle1 + circle2
result2 = circle1 - circle2
print(result)
print(result1)
print(result2)