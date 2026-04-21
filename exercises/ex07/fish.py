"""File to define Fish class."""


class Fish:
    """Fih in river exosystem"""

    age: int

    def __init__(self):
        """assigns fih to age 0"""
        self.age = 0
        return None

    def one_day(self):
        """increases fih age by 1 each day"""
        self.age += 1
        return None
