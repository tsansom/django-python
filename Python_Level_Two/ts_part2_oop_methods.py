class Circle():

    pi = 3.14159

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi*self.radius**2

    def set_radius(self, new_radius):
        self.radius = new_radius

myc = Circle(radius=3)
# myc.radius = 100
myc.set_radius(100)
print(myc.area())
