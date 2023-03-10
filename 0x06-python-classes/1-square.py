#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and a method that
sets its size.
"""


class Square():
    """create a class."""

    def __init__(self, size):
        """Set the necessary attributes for the Square object.
        
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
