"""File to define Bear class."""


class Bear:
    """A bear object for river"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize bear object with age 0"""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """every day the bear age increases by 1 and its hunger goes down 1"""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """assigns the hunger attribute to number of fish"""
        self.hunger_score += num_fish
        return None
