"""Decomposing a larger program into small subprograms
Writing multiple small functions that each solve a single problem
Writing functions that call other functions
Writing a “main” function that orchestrates the program's execution"""

__author__: str = "730894533"


def main_planner(guests: int) -> None:
    """Calls all previous functions to make a giant statement"""
    # Wish we went over in class or on the slides- used what I knew + some help and trial and error
    bags: int = tea_bags(people=guests)
    treat_number: float = treats(people=guests)
    total_number: float = cost(tea_count=bags, treat_count=(treat_number))
    # Not sure what im doing here or what to put for variables,prints etc.
    print(("A Cozy Tea Party for " + str(guests)) + " People!")
    print("Tea Bags: " + str(bags))
    print("Treats: " + str(treat_number))
    print("Cost: $" + str(total_number))


def tea_bags(people: int) -> int:
    """returns tea bags needed based on on # of guests"""
    return people * 2


tea_bags(people=4)


def treats(people: int) -> float:
    """returns number of treats x1.5 # of tea_bags"""
    return tea_bags(people=people) * 1.5


def cost(tea_count: int, treat_count: float) -> float:
    """returns cost of tea bags and cost of treat_count"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How Many Guests are Attending your Tea Party? ")))
