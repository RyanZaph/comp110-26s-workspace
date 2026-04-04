"""EX02 - Chardle - a cute step toward Wordle."""

__author__: str = "730894533"


def input_word() -> str:  # does no parameter mean none
    """a function lets you input a 5 letter word and prints error if its not"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        print(word)
    return word


# delete


def input_letter() -> str:
    """function that lets you input a letter and if not returns error"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1 and type(letter) == str:
        print(letter)
    else:
        print("Error: Character must be a single character.")
        exit()
    return letter


# delete

# forgot to call fucntion


def contains_char(word_2: str, letter_2: str) -> None:
    """function that searches for letter in word"""
    print("Searching for " + letter_2 + " in " + word_2)
    count = 0
    """count how mnay times letter appears in word"""
    if len(letter_2) != 1:
        print("Error: Character must be a single character.")
    if letter_2 == word_2[0]:
        # print("Searching for " + letter_2 + " in " + word_2)
        print(letter_2 + " found at index 0")
        count += 1
    if letter_2 == word_2[1]:
        print(letter_2 + " found at index 1")
        count += 1
    if letter_2 == word_2[2]:
        print(letter_2 + " found at index 2")
        count += 1
    if letter_2 == word_2[3]:

        print(letter_2 + " found at index 3")
        count += 1
    if letter_2 == word_2[4]:
        print(letter_2 + " found at index 4")
        count += 1

    if count == 0:
        print("No instances of " + letter_2 + " found in " + word_2)
    elif count == 1:
        print("1 instance of " + letter_2 + " found in " + word_2)
    else:
        print(str(count) + " instances of " + letter_2 + " found in " + word_2)


def main() -> None:
    """calls all of the functions"""  # I already made this statement
    final_word: str = input_word()
    final_letter: str = input_letter()
    contains_char(word_2=final_word, letter_2=final_letter)


if __name__ == "__main__":
    main()

    # do I need to put this twice? should have put this

# def contains_char(word): str, (letter): str-> str:

# what does thoserror mean
