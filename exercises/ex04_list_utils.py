__author__: str = "730894533"


def all(
    items: list[int], match: int
) -> bool:  # I should make a definition not like the lists.py
    index: int = 0
    if len(items) == 0:
        return False  # false doenst need paramters
    while index < len(items):
        if (
            items[index] != match
        ):  # do false first so it can iterate through all to return true
            return False
        index = index + 1  # use regardless
    return True


def max(largest: list[int]) -> int:
    index: int = 0
    if len(largest) == 0:
        raise ValueError("max() arg is an empty List")  # new way!
    max_value: int = largest[
        0
    ]  # forgot to declare a local variable was trying to create another paramtere
    while index < len(largest):
        if largest[index] > max_value:
            max_value = largest[index]  # try not to use fix
        index = index + 1
    return max_value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    index: int = 0
    while index < len(list_2):
        ind_char_1 = list_1[index]
        ind_char_2 = list_2[index]
        if ind_char_1 != ind_char_2:
            return False
        index = index + 1
    return True


a: list[int] = [1, 2, 3]  # do I need this
b: list[int] = [4, 5, 6]


def extend(list_X: list[int], list_Y: list[int]) -> None:
    index: int = 0
    while index < len(list_Y):
        list_X.append(list_Y[index])
        index = index + 1
    print(list_X)
