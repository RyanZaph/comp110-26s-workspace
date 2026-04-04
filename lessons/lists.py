"""Function will list syntax"""

# Initialize a emty List of floats with the paramter my_number
my_number: list[float] = []  # can also be list[float] = list() which is constuctor

my_number.append(1.5)

print(my_number)

"initializing already populated list"
# Create a list called game_pointsthat stores the following numbers:102, 86, 94

game_pointsthat: list[int] = [102, 86, 94, 94]
print(game_pointsthat[2])  # for accessing specific items

# change 86 to 72
game_pointsthat[1] = 72

# print the length
print(len(game_pointsthat))

# remove an item in the list
print(
    game_pointsthat.pop(1)
)  # can also remove the element and print it to do something with it

print(game_pointsthat)
