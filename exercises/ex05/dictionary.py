"""EX05 - Dictionary Utility Functions."""

__author__: str = "730894533"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary.

    Raises:
        KeyError: If the input dictionary contains duplicate values.
    """
    inverted: dict[str, str] = {}
    for key, value in dictionary.items():
        if value in inverted:
            raise KeyError(f"Duplicate value {value} found in input dictionary")
        inverted[value] = key
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Return the most common color in the dictionary.

    If the dictionary is empty, return an empty string.
    """
    counts: dict[str, int] = {}
    for color in dictionary.values():
        counts[color] = counts.get(color, 0) + 1

    most_common: str = ""
    max_count: int = 0
    for color, count_value in counts.items():
        if count_value > max_count:
            max_count = count_value
            most_common = color
    return most_common


def count(items: list[str]) -> dict[str, int]:
    """Count how many times each string appears in a list."""
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter.

    Words that include any non-letter characters are ignored entirely.
    """
    grouped: dict[str, list[str]] = {}
    for word in word_list:
        if not word.isalpha():
            continue
        first_letter = word[0].lower()
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(word)
    return grouped


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> dict[str, list[str]]:
    """Add a student to the attendance log for a given day.

    If either the day or student is empty, the attendance log is unchanged.
    """
    if day == "" or student == "":
        return attendance_log

    if day not in attendance_log:
        attendance_log[day] = []

    if student not in attendance_log[day]:
        attendance_log[day].append(student)
    return attendance_log
