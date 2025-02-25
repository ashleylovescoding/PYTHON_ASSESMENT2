class Shape:
   def area(self):
       return 0
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius,pi):
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * self.radius * self.radius

Rectangle = Rectangle(100, 100)
Circle = Circle(100, 3.142857)
print(Rectangle.area())
print(Circle.area())
