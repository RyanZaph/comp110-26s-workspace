def get_first(input_list: list[str]) -> str:
    """Returns the first element of the list without modifying it."""
    if len(input_list) == 0:
        return ""
    return input_list[0]


def remove_first(input_list: list[str]) -> None:
    """Removes the first element of the list. Does not return anything."""
    if len(input_list) > 0:
        input_list.pop(0)


def get_and_remove_first(input_list: list[str]) -> str:
    """Returns AND removes the first element of the list."""
    if len(input_list) == 0:
        return ""
    # pop(0) removes the item at index 0 and returns it
    return input_list.pop(0)

def test_remove_first_empty_behavior() -> None:

def empty_list():
    """Testing an edge case: does the list actually end up empty?"""
    names = ["Alice", "Bob"]
    names == []  # This checks if the result is an empty list
