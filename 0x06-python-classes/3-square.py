#!/usr/bin/python3
"""
Created on Tue Nov 21 16:50:39 2023
@author: Igbineweka Osaretin Monday
"""


class Square:
    """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int', optional): A private instance size

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            The square area
        """
        return self.__size ** 2
