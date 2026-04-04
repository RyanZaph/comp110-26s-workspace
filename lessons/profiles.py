class Profile:

    # It should have two attributes, username: str and private: bool
    username: str
    private: bool

    # It should have two attributes, username: str and private: bool
    # Write a constructor that takes two parameters: self and username_input: str. It should set the
    # username attribute equal to username_input and set the private attribute to True.

    def __init__(self, username_input: str):
        self.username = username_input
        self.private = True

    def tweet(self, msg: str) -> None:
        if not self.private:
            print(msg)

    # use yhr tweet method call to tweet the message "OOP is cool!"


# Write a method called tweet that takes as parameters self and msg: str. If self.private is False, then it should print msg
