ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("mint")
ice_cream["chocolate"]
ice_cream["vanilla"] = 10
"chocolate" and "vanilla" in ice_cream
print(ice_cream["pecan"])
print(len(ice_cream))
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

# def grade_bump(gradebook: dict[str, str] = {"eggby": "A", "Eggsy": "F"}) -> None:


def grade_bump( student: str, gradebook: dict[str, str]) -> None:
# """Mutates a gradebook by bumping a student's grade."""
# if gradebook[student] == "A":
#     gradebook[student] = "A+"
# else:
#     gradebook[student] = "A"
#  print(grade_bump)
