def check_first_letter(word: str, letter: str) -> str:
    """Return match if letter is first char of word, else return no match"""
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="happy", letter="s"))


def get_weather_report(weather: str) -> str:
    if weather == "rainy" or weather == "cold":
        print("bring a jacket")
    elif weather == "hot":
        print("Keep cool Out there!")
    else:
        print("I don't recognize this weather")
    return weather


get_weather_report(weather="cold")
