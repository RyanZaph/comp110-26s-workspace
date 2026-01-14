"""My First Excercise in COMP110!"""

__author__ = "730894533"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


greet("Ryan")

greet(name="Student")


if __name__ == "__main__":
    print(greet(name=input("What is your name?")))
