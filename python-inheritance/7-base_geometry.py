#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value: must be integer > 0"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
