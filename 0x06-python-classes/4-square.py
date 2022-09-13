#!/usr/bin/python3


class Square:
    """
    creates square
    """

    def __init__(self, size=0):
        """
        initializes square
        Args:
            size: size of side of square
        """
        self.__size = size

    @property
    def size(self):
        """
        finds size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        validates size is an integer that is greater than zero
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        finds area of square
        Returns:
            area of square
        """
        return self.__size ** 2i
