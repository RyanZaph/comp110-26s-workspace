"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730894533"

"""Make class RIver"""


class River:

    day: int
    """tells you what day of the rivers lifecycle you are modeling"""
    fish: list[Fish]
    """stores the rivers fish population"""
    bears: list[Bear]
    """tores the rivers bear population"""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """checks the age of the fish and the beras to see if they should be alive or not"""
        alive_fish_list: list[Fish] = []
        alive_bear_list: list[Bear] = []

        # creates new fish list, for element in list (fish) if age is >= 3 then append that element(fish) to new list, same for bear
        for fish in self.fish:
            if fish.age <= 3:  # if fish is 3 or younger append to alive fish list
                alive_fish_list.append(fish)
        self.fish = alive_fish_list  # this list become the new list
        for bear in self.bears:  # if bear is 5 or younger append to alive bear list
            if bear.age <= 5:
                alive_bear_list.append(bear)
        self.bears = alive_bear_list  # this becomes new list
        # Simulate Fish repopulation
        return None

    def bears_eating(self):
        """if more than 5fish each bear then the fish eats 3 of them remov for bear eating them"""
        for bear in self.bears:
            if len(self.fish) >= 5:
                bear.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """ "Checks the bear hunger score, if they have 0 its removed from the list and make new list with surviving bears"""
        full_bear_list: list[Bear] = []
        full_bear_list = self.bears
        for bear in self.bears:
            if (
                bear.hunger_score < 0
            ):  # if the bear is not hungry ie less than 0 then add that bear to surviving list else rip
                full_bear_list.remove(bear)
        self.bears = full_bear_list  # this becones new list
        # Remove old Fish and Bear's from River
        return None

    def repopulate_fish(self):
        """ "Method that makes it that for every 2 fish in the water they will produce 4 new baby fish and add them to total fish list"""
        num_new_fish: int = len(self.fish) // 2 * 4
        for _ in range(num_new_fish):
            self.fish.append(
                Fish()
            )  # creates new fish object for the baby fish and adds it to total list
        # Simulate Bear repopulation
        return None

    def repopulate_bears(self):
        """Makes it to were if there are 2 bears in the population, there will be 1 new bear produced and added to total nbear list"""
        num_new_bears: int = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def __str__(self) -> str:
        return f"~~~ Day {self.day}: ~~~\n Fish Population: {len(self.fish)}\n Bear population: {len(self.bears)}"

    """Where x is the current day of the river, y is the number of Fish in the river, and z is the number of Bears in the river"""

    def __add__(self, r: River) -> River:
        """adds the population of the two rivers, self, and r and puts them into a new river"""
        larger_river_fish: int = len(self.fish) + len(r.fish)
        larger_river_bears: int = len(self.bears) + len(r.bears)
        new_river: River = River(larger_river_fish, larger_river_bears)
        return new_river

    def __mul__(self, factor: int) -> River:
        """multiplies the population fo two rivers self and r by facotr and adds them to a new river"""
        mul_fish: int = len(self.fish) * factor
        mul_bears: int = len(self.bears) * factor
        mul_river: River = River(mul_fish, mul_bears)
        return mul_river

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()  # for every bear in river if 5+ fish in river remove 3 fish for eating
        # Remove hungry Bear's from River
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        print(self)

    def remove_fish(self, amount: int):
        """accounts for overpopulation :)"""
        for _ in range(amount):  # every item in range of fish amount
            self.fish.pop(0)  # use parenthesis for accessign pop index
        return None

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()
        return None
