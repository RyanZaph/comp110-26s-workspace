from __future__ import (
    annotations,
)  # use when  defining a method that returns its own type (e.g. a method in our Point class that returns a Point)


class Point:    #blueprint to create object

    x: float        #attributes
    y: float

    def __init__(self, x_init: float, y_init: float): #used to initilize specif values for the attributes of the class when we create an object
        self.x = x_init     
        self.y = y_init

    def scale_by(self, factor: int) -> None: 
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)
