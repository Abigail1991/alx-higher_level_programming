#!/usr/bin/python3
""" Square Module"""


class Square():
    """Class representing a square"""

    def __init__(self, size):
        """ Sets the necessary attributes for the Square object
        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
