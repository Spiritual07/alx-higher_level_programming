#!/usr/bin/python3
"""
Created on Tue Nov 21 15:59:54 2023
@author: Igbineweka Osaretin Monday
"""


class Square:
    """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int'): A private instance size
        """
        self.__size = size
