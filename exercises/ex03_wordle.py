__author__: str = "730894533"


def input_guess(secret_word_len: int) -> str:
    """looks for your input of word and sees if it matches the length of the secret word"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != (secret_word_len):
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
        # had to cut stuff out for bloat (office hours)
    return guess


def contains_char(secret: str, char_match: str) -> bool:  # imported from cq (edit?)
    """This function searches for a specific character in a word to see if there are any occurences of it"""
    assert len(char_match) == 1
    index: int = 0
    while index < len(secret):
        if secret[index] == char_match:
            return True
        index = index + 1
    return False


def emojified(
    guess_scrt: str, secret_word: str
) -> (
    str
):  # office hours was not sure how to begin implementing, always make variables for complex functions and think logically step by step
    """compares input word and secret word of equal length and assigns emoji colors to the correct, false, or wrong positioned characters"""
    assert len(guess_scrt) == len(secret_word)
    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"
    index: int = 0
    output: str = ""  # ?
    while index < len(secret_word):
        if (
            guess_scrt[index] == secret_word[index]
        ):  # how do I go about implementing this?
            output = output + GREEN_BOX
        elif contains_char(secret=secret_word, char_match=guess_scrt[index]):  # think
            output = output + YELLOW_BOX
        else:
            output = output + WHITE_BOX
        index = index + 1
    return output


def main(secret1: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    victory: bool = False
    while (
        turn <= 6 and not victory
    ):  # why not make a function that keeps output of emojified function? make it a varibale isnated
        print(f"=== Turn {turn}/6 === ")
        guess: str = input_guess(len(secret1))
        print(emojified(guess, secret1))  # should I only print once
        if guess == secret1:
            victory = True
        else:
            turn = turn + 1
    if turn <= 6 and victory == True:
        print(f" You won in {turn}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret1="codes")  # what to put here
