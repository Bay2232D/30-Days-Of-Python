class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# membuat objek rectangle
my_rectangle = Rectangle(5, 6)

# memanggil method area pada objek rectangle
result1 = my_rectangle.area()
print(result1) # output: 30

# membuat objek circle
my_circle = Circle(7)

# memanggil method area pada objek circle
result2 = my_circle.area()
print(result2) # output: 153.86
