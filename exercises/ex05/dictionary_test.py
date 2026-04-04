"""Tests for the EX05 dictionary utilities."""

__author__: str = "730894533"

from exercises.ex05.dictionary import (
    alphabetizer,
    count,
    favorite_color,
    invert,
    update_attendance,
)


def test_invert_1() -> None:
    """Invert a dictionary with basic string pairs."""
    assert invert({"one": "two", "three": "four"}) == {"two": "one", "four": "three"}


def test_invert_2() -> None:
    """Invert a dictionary with other string values."""
    assert invert({"slam": "dunk", "home": "run"}) == {
        "dunk": "slam",
        "run": "home",
    }


def test_invert_3() -> None:
    """Return an empty dictionary when input is empty."""
    assert invert({}) == {}


def test_invert_4_duplicate_values_raise_key_error() -> None:
    """Raise KeyError when duplicate values are present."""
    try:
        invert({"a": "x", "b": "x"})
        raise AssertionError("Expected KeyError for duplicate values")
    except KeyError:
        pass


def test_favorite_color_1() -> None:
    """Return the most common color from a small dictionary."""
    result = favorite_color(
        {
            "Greg": "green",
            "eggark": "red",
            "housayninmyarocky": "blue",
            "Gormy": "green",
        }
    )
    assert result == "green"


def test_favorite_color_2() -> None:
    """Return a tied color when two colors have equal highest counts."""
    result = favorite_color(
        {
            "Greg": "green",
            "eggark": "red",
            "housayninmyarocky": "green",
            "Gormy": "red",
        }
    )
    assert result == "green"


def test_favorite_color_3() -> None:
    """Return an empty string for an empty input dictionary."""
    assert favorite_color({}) == ""


def test_favorite_color_4_single_entry() -> None:
    """Return the single favorite color when only one person is present."""
    assert favorite_color({"Ariel": "purple"}) == "purple"


def test_count_1() -> None:
    """Count repeated words in a list."""
    assert count(["egg", "egg", "bannana", "milk"]) == {
        "egg": 2,
        "bannana": 1,
        "milk": 1,
    }


def test_count_2() -> None:
    """Count strings including special characters."""
    assert count(["egg", "#!902", "apple", "egg"]) == {
        "egg": 2,
        "#!902": 1,
        "apple": 1,
    }


def test_count_3() -> None:
    """Return an empty dictionary for an empty list."""
    assert count([]) == {}


def test_count_4_duplicate_values() -> None:
    """Count a list with the same value repeated multiple times."""
    assert count(["same", "same", "same"]) == {"same": 3}


def test_alphabetizer() -> None:
    """Group alphabetical words while ignoring non-alpha entries."""
    assert alphabetizer(["egg", "Eggarkopoly", "shoomy"]) == {
        "e": ["egg", "Eggarkopoly"],
        "s": ["shoomy"],
    }


def test_alphabetizer_2() -> None:
    """Ignore words with digits or punctuation."""
    result = alphabetizer(
        ["greggertosphagin", "slatt", "balashba", "cregandicliffs", "5467389"]
    )
    assert result == {
        "g": ["greggertosphagin"],
        "s": ["slatt"],
        "b": ["balashba"],
        "c": ["cregandicliffs"],
    }


def test_alphabetizer_3() -> None:
    """Return an empty dictionary for an empty input list."""
    assert alphabetizer([]) == {}


def test_alphabetizer_4_special_characters_are_removed() -> None:
    """Ignore words that contain special characters."""
    assert alphabetizer(["@hello!", "ABC-123", "z?", "two_two"]) == {}


def test_update_attendance_1() -> None:
    """Add a student on a new day."""
    attendance_log: dict[str, list[str]] = {
        "Monday": ["Greg", "Craig"],
        "Tuesday": ["Eggby"],
    }
    assert update_attendance(attendance_log, "Wednesday", "Pitzareuqe") == {
        "Monday": ["Greg", "Craig"],
        "Tuesday": ["Eggby"],
        "Wednesday": ["Pitzareuqe"],
    }


def test_update_attendance_2() -> None:
    """Append a student to an existing day."""
    attendance_log: dict[str, list[str]] = {
        "Monday": ["Greg", "Craig"],
        "Tuesday": ["Eggby"],
    }
    assert update_attendance(attendance_log, "Tuesday", "Jame") == {
        "Monday": ["Greg", "Craig"],
        "Tuesday": ["Eggby", "Jame"],
    }


def test_update_attendance_3() -> None:
    """Leave attendance unchanged for empty day and student."""
    attendance_
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     "Craig"],
        "Tuesday": ["Eggby"],
    }
