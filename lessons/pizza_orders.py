"""Practice the basic syntax of ODP"""

# Define a class called Pizza


class Pizza:

    glutten_free: bool
    size: str
    num_toppings: int

    def __init__(self, gf: bool, sz: str, top: int):
        self.glutten_free = gf
        self.size = sz
        self.num_toppings = top

    def price(self, price_bump: float) -> float:
        """return price of pizza object"""
        total: float = price_bump
        # Size “small” costs $5.25, other sizes cost $7.50
        if self.size == "small":
            total = 5.25
        else:
            total = 7.50
        # # Each topping is $.25
        total += self.num_toppings * 0.25
        # If gluten free, add $1
        if self.glutten_free is True:
            total += 1.0
        return total


# Define a function outside the class that uses the class
    def num_orders(orders: list[Pizza]) -> int:
    return len(orders)


# Instatiate your class
alyssas_order: Pizza = Pizza(False, "small", 2)  # type: ignore # <- Constructor
jacks_order: Pizza = Pizza(True, "Large", 4)  # type: ignore # <- new pizza object\
alyssas_order.glutten_free = False
alyssas_order.size = "small"
alyssas_order.num_toppings = 2
jacks_order.size = "Large"

print(alyssas_order.price(1.0))
print(jacks_order.price(0.0))

pizza_list: list[Pizza] = [alyssas_order, jacks_order, Pizza(False, "small", 0)]
print(len(pizza_list))  # ugly
print(num_orders(pizza_list))
