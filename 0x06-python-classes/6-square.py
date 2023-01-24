#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and its size and its
position on the screen, checking if the given values are right, and a setter
and getter methods to set or get them. There's also an area method that return
the area of the square, another one that handles the print of the square.
"""


class Square():
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Sets the necessary attributes for the Square object.
        Args:
            size (int): the size of one edge of the square.
            position (tuple): the coordinates of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get or set the position of the square."""
        return self.__position

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.size ** 2

    def my_print(self):
        """Prints the square with the # character on stdout."""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
