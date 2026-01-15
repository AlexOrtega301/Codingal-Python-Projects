import math

# Codingal Project: hi Teacher!
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class RegularPolygon(Shape):
    def __init__(self, sides, side_length):
        super().__init__("Regular Polygon")
        self.sides = sides
        self.side_length = side_length

    def area(self):
        return (self.sides * (self.side_length ** 2)) / (4 * math.tan(math.pi / self.sides))

# What the user will see!
print("Geometry Area Calculator")

while True:
    print("\nChoose a shape:")
    print("1 - Rectangle")
    print("2 - Triangle")
    print("3 - Circle")
    print("4 - Regular Polygon")
    print("5 - Quit")

    choice = input("Option: ")

    if choice == "1":
        w = float(input("Enter width: "))
        h = float(input("Enter height: "))
        shape = Rectangle(w, h)

    elif choice == "2":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        shape = Triangle(b, h)

    elif choice == "3":
        r = float(input("Enter radius: "))
        shape = Circle(r)

    elif choice == "4":
        s = int(input("Enter number of sides: "))
        l = float(input("Enter length of each side: "))
        shape = RegularPolygon(s, l)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
        continue

    print(f"The area of the {shape.name} is: {shape.area():.2f}")
