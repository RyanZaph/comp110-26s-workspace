"""practicing for loops"""

pet_names: list[str] = ["Louie", "Bo", "Bear"]
good_boy: list[str] = []
for elem in pet_names:
    good_boy.append(elem)
    print("Good boy, " + elem + "!")

# or


def celebrate(pet_names: list[str]) -> None:
    for good_boy in pet_names:
        msg: str = "Good boy, " + good_boy + "!"
        print(msg)
