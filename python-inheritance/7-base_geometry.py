#!/usr/bin/python3
"""
Defines BaseGeometry class.
"""

class BaseGeometry:
    """
    Base class for geometry.
    """

    def area(self):
        """
        Raises exception for unimplemented area.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an int > 0.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
