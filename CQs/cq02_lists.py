"""Mutating lists"""

__author__: str = "730894533"

a: list[int] = [1, 2, 3]


def manual_append(word: list[int], num: int) -> None:
    word.append(num)


def double(word: list[int]) -> None:
    index: int = 0
    while index < len(word):
        word[index] = word[index] * 2
        index = index + 1


double(list_2)
print(list_1)
print(list_2)
