__author__: str = "730894533"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0  # number of times character appears
    index: int = 0  # tracks of every instance of a charcater in phrase
    while index < len(phrase):
        if search_char == phrase[index]:
            count = count + 1
        index = index + 1
    return count


def get_evens(numbers: str) -> str:
    evens: str = ""
    index: int = 0
    while index < len(numbers):
        if int(numbers[index]) % 2 == 0:
            evens = evens + numbers[index]
        index = index + 1
    return evens


get_evens(numbers="6758493029202")
