"""Tracy Worden MIS532 - EX05 Create and test a Rectangle class. This must be placed inside a "shapes.py" module
and tested using your ex05 main program. Objects of a rectangle class should have a radius,
should be printable to the screen, and show have two methods -- area and perimeter
The Rectangle class must include an __init__ method that accepts a length and width
 (and default to 1 if none are given)"""

import shapes

rectangle1 = shapes.Rectangle(10, 45)
rectangle2 = shapes.Rectangle()
rectangle3 = shapes.Rectangle(4)

print("\nRectangle 1")
print(rectangle1)
print(f"area = {rectangle1.area()}")
print(f"perimeter = {rectangle1.perimeter()}")

print("\nRectangle 2")
print(rectangle2)
print(f"area = {rectangle2.area()}")
print(f"perimeter = {rectangle2.perimeter()}")

print("\nRectangle 3")
print(rectangle3)
print(f"area = {rectangle3.area()}")
print(f"perimeter = {rectangle3.perimeter()}")
