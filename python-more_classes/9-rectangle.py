#!/usr/bin/python3
"""
Real definition of a rectangle
"""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize new rectangle instances."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width. Raises TypeError or ValueError."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height. Raises TypeError or ValueError."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """print rectangle  usinng #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                result += "\n"
        return result

    def __repr__(self):
        """ return a string representation of the
        rectangle to be able to recreate a new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Bye rectangle...  when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area
        TypeError if not isinstance or Rectangle
        Returns rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
