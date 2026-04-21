class Game_Collection:  # class

    inventory: list[str]  # attributes
    wishlist: list[str]
    budget: float

    def __init__(
        self, curr_inventory: list[str], wish: list[str], start_budget: float):  # make constructor and initilize attributees
        self.inventory = curr_inventory
        self.wishlist = wish
        self.budget = start_budget

    def purchase(self, name: str, cost: float):  # write method to see waht cost
        if cost < self.budget:  # do not use self to refer to cost, used for previous object
            self.budget -= cost
            self.inventory.append(name) #append name of game to wishlist
            idx: int = 0 
            while idx < len(self.wishlist): # iterates through the list to see if game in wishlist if it is then remove it.
                curr_game: str = self.wishlist[idx]
                if curr_game == name:
                    self.wishlist.pop(idx)
                idx += 1
        elif cost > self.budget: # could also just write else:
            print("Sorry! Not enough money!")

    def __add__(self, new_game: str) -> Game_Collection: # calls self 
        new_wishlist: list[str] = []
        #copy over self.wishlist items
        for item in self.wishlist:
            new_wishlist.append(item)
        #add new_game to new wishlist
        new_wishlist.append(new_game)
        new_collection: Game_Collection = Game_Collection(curr_inventory=self.inventory, wish=self.wishlist, self.budget)


my_games: Game_Collection = Game_Collection(curr_inventory =("Sims"), wish = ("Witcher"), start_budget= 50.75) # make magic method with game collection = to game collecton with following paramteres SIMS and WITCHER
my_games.purchase("Stardew", 40.25)-
print(my_games.inventory)
print(my_games.budget)

my_games.purchase("Witcher", 60.00)

ryans_games: Game_Collection = my_games + "Mario"
print(ryans_games.wishlist)
print(my_games.wishlist)