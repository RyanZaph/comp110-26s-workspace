"""practice using while loops to iterate over n string"""


def find_low_card(cards: str) -> int:
    index: int = 0
    low_card: int = int(cards[0])  # converts first character in cards into an integer
    while index < len(cards):
        current_card: int = int()
        cards[index]
        # The "card" we are currently looking at in the loop do something
        if current_card < low_card:
            low_card = current_card
        index = index + 1
    return low_card


print(find_low_card(cards="324310"))
