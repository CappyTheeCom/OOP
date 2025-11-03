import math

class Shape:
    pass

class Circle(Shape):
    def __init__(self, a, b, raduis, sin, cos):
        self.a = a
        self.b = b
        self.raduis = raduis
        self.sin = sin
        self.cos = cos

        self.area = Circle.area(raduis)
    
    def area(radius):
        return radius ** 2 * math.pi
    
    def circumfrence(radius):
        return 2 * radius * math.pi

    def point_y(self):
        __point_y = self.raduis * self.sin + self.b
        print(f"User vertical point: {__point_y:.2f}")

    def point_x(self):
        __point_x = self.raduis * self.cos + self.a
        print(f"Horizontal point: {__point_x:.2f}")

    def __str__(self):
        return super().__str__()

# Get user input
point_a = float(input("Enter horizontal number: "))
point_b = float(input("Enter vertical number: "))
base_raduis = float(input("Enter radius value: "))

# For the trigonometric calculations, let's use degrees and convert to radians
sin_deg = float(input("Enter the degrees for sin: "))
cos_deg = float(input("Enter the degrees for cos: "))
sin_val = math.sin(math.radians(sin_deg))
cos_val = math.cos(math.radians(cos_deg))

# Create objects with correct arguments
circle = Circle(point_a, point_b, base_raduis, sin_val, cos_val)
print(circle.area)
circle.circle_comp()
circle.point_x()
circle.point_y()

print(circle)
