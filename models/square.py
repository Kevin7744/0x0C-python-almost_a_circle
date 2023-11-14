#!/usr/bin/python3
""" Class square that inherits from Rectangle """

from .rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from class rectangle """
    def __init__(self, size, x=0, y=0,id=None):
        """ Initializes an instance of class Square """
        super().__init__(size, size, x, y, id)
