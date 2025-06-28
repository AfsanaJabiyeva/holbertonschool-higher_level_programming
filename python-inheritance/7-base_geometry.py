#!/usr/bin/python3
""" a class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """comment"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """comment"""
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be greater than 0")
