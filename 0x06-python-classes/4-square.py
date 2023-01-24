#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and its size and checking
if the given values are right, and a setter and getter methods to set or get
it. There's also an area method that returns the area of the square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0):
        """Sets the necessary attributes for the Square object.
         Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""

        return self.__size ** 2
