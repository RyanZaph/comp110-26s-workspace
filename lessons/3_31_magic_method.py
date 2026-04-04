class ShoppingGuide:

    groceries: list[str]
    budget: float
    store: str

    def __Init__(self, groceries: list[str], budget: float, store: str) #name of constructor and returns self
        self.groceries = groceries
        self.budget = budget
        self.store = store

# Write a class called ShoppingGuide 
# It should have three attributes, groceries: list[str], budget: float, and store: str
# Write a constructor that takes four parameters:
# self, groceries: list[str], budget: float, and store: str.
# It should update the attributes accordingly.
# Write a __str__ magic method that gives me all the information of a ShoppingGuide object

    def __str__(self) -> str:
        info: str = f"Go to {self.store} and buy {self.groceries} with ${self.budget}"
        return info 
    
    # Write a magic method __add__ that takes as parameters self, more_money: float.
# ○ It should return a new ShoppingGuide object with the same attribute values except it should
# add more_money to the budget
    def __add__(self, more_money: float) -> ShoppingGuide:
        other_guide: ShoppingGuide = ShoppingGuide(self.groceries, self.budget + more_money, self.store)
        return other_guide

# Instantiation
#● Create a new variable my_plan that is reference to a ShoppingGuide object with the groceries
#[“apples”, “kiwi”], the budget $5.55, and the store “Food Lion”.
#● Now create another variable AJs_plan that is my_plan but with $2.12 added to the budget
#● Print out AJs_plan
my_plan: ShoppingGuide = ShoppingGuide(("apples", "kiwi"), 5.55, "Food Lion")
print(my_plan)
AJs_plan: ShoppingGuide = my_plan +2.12
print(AJs_plan)