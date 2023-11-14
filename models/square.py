#!/usr/bin/python3
""" Class square that inherits from Rectangle """

from .rectangle import Rectangle


class Square(Rectangle):
    """ Inherits from class rectangle """
    def __init__(self, size, x=0, y=0,id=None):
        """ Initializes an instance of class Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the instance """
        a = self.id
        b = self.width
        c = self.x 
        d = self.y
        return "[Square] ({}) {}/{} - {}".format(a, c, d, b)

    @property
    def size(self):
        """ retrieves the attribute size """
        return self.width

    @size.setter
    def size(self, value):
        """ Validate and sets the attribut size """
        self.width = value
        self.heght = value
