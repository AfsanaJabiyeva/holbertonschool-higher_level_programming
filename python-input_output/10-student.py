#!/usr/bin/python3
"""Defines a Student class with attribute filtering in to_json."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student.

        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                k: getattr(self, k) for k in attrs if hasattr(self, k)
            }
        return self.__dict__
