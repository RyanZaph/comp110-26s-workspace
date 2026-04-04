from list_fns import get_first, remove_first, get_and_remove_first 


def test_get_first_name_output() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Ben"]

    assert get_first(names) == "Alyssa"


def test_get_and_remove_first_names_output() -> None:
    names: list[str] = ["Alyssa", "Izzi", "Ben"]

    assert get_and_remove_first(names) == "Alyssa"


def test_remove_first_names_behavior() -> None:
    "test remove behavior on names"
    names: list[str] = ["Alyssa", "Izzi", "Ben"]

    remove_first(names)
    assert names == ["Izzi", "Ben"]


def test_get_and_remove_names_behavior() -> None:
    "test get and remove behavior on names"
    names: list[str] = ["Alyssa", "Izzi", "Ben"]

    get_and_remove_first(names)
    assert names == ["Izzi", "Ben"]


def test_get_first_names_behavior() -> None:
    "Test get first behavior on names"
    names: list[str] = ["Alyssa", "Izzi", "Ben"]
    
    get_first(names)
    assert names == ["Alyssa", "Izzi", "Ben"]

def test_remove_first_empty_behavior() -> None:
    
def test_empty_list_behavior():
    """Testing an edge case: does the list actually end up empty?"""
    names = ["Alice", "Bob"]
    empty_list(names)
    assert names == []  # This checks if the result is an empty list