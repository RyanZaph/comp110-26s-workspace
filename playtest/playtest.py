def contains_char(input_word: str, char_match: str) -> bool:  # imported from cq (edit?)
    """This function searches for a specific character in a word to see if there are any occurences of it"""
    assert len(char_match) == 1
    index: int = 0
    while index < len(input_word):
        if input_word[index] == char_match:
            return True
        index = index + 1
    return False


contains_char("foot", "o")
type: str = input()
