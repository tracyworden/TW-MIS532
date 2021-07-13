"""Class to calculate a rectangle"""
import math


class Rectangle:

    # init
    def __init__(self, length=1, width=1):
        """Initialize the Rectangle Object"""

        self.length = length
        self.width = width
        self.radius()

    # methods area, perimeter
    def area(self):
        """Calculate area of a rectangle: A = w * l"""
        return self.width * self.length

    def perimeter(self):
        """Calculate perimeter of a rectangle P = 2 * w + 2 * l"""
        return 2 * self.width + 2 * self.length

    def radius(self):
        """Calculate radius of a rectangle r = d/2 """
        diameter = math.sqrt(self.length ** 2 + self.width ** 2)
        return diameter / 2

    # special methods __str__
    def __str__(self):
        return f"length = {self.length} width = {self.width} \nradius = {self.radius()}"
