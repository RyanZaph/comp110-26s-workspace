"""practicing for loops"""

pet_names: list[str] = [
    "Louie",
    "Bo",
    "Bear",
]  # this works but only for the specific list so not assignable
good_boy: list[str] = []
for elem in pet_names:
    good_boy.append(elem)
    print("Good boy, " + elem + "!")

# or


def celebrate(pet_names: list[str]) -> None:
    for index in range(0, len(pet_names)):
        (good_boy) in (pet_names):  # dont have to decalre good_boy vafriable becuase it assiings it to elements in list
        msg: str = index + "Good boy, " + good_boy + "!"  # look at this after class
        print({msg})


celebrate(pet_names)


def get_orders(orders: dict[str, int]) -> None:
    for flavor in orders:  # flavor is the key
        num_orders: int = orders[flavor]  # orders at that key is the value]
        print(f"{flavor} has {num_orders} orders.")
