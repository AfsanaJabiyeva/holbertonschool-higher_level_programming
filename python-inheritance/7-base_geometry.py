#!/usr/bin/python3
"""Defines BaseGeometry class with area and integer_validator methods"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an Exception for area method not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer

        Args:
            name (str): name of the parameter
            value: value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
