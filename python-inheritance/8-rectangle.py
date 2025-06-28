#!/usr/bin/python3
"""Rectangle module."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle with validated width and height."""

    def __init__(self, width, height):
        """Initialize with width and height as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
