from __future__ import annotations

__author__ = "730472086"

class Node:

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str: # needed to put this here not at the bottom
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    if head is None: # checks if we reached the end of the listd
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0: # this is whtat we want so return value of node
        return head.value
    else:
        return value_at(head.next, index - 1) # not correct so we go back until we reach index 0  
    

def max(head: Node | None) -> int:
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None: # if the last node is the largest/only node then return it
        return head.value
    max_val = max(head.next) #assigns max value to current nodes value but if next node is larger then return head value else return max
    if head.value > max_val:
        return head.value
    else:
        return max_val 

# logic here,

# linked list: [10] -> [20] -> [30] -> None
#Node 10 calls max on Node 20. (Waits...)
# Node 20 calls max on Node 30. (Waits...)
# Node 30 sees its next is None. It returns 30.
# Node 20 resumes. It compares its value (20) to the returned value (30). Since 30 is bigger, it returns 30.
# Node 10 resumes. It compares its value (10) to the returned value (30). Since 30 is bigger, it returns 30.

# Linkify (slice technique)
# >>> items = [10, 20, 30, 40]
#>>> items[1] return index 1 which is 20
#20
#>>> items[1:3] return index 1 value (inclusive) to 3 (exclusive) so just 2 and 3
#[20, 30]
#>>> items[:3] defualts to index 0 if left out
#[10, 20, 30]
#>>> items[1:] defaults to length o flist if end lef out
#[20, 30, 40]

def linkify(items: list[int]) -> Node | None:
    if len(items)  == 0:
        return None
    return Node(items[0], linkify(items[1:])) # makes a node with list at index 0 and then iterates through the list by calling linkify (recursion) and goes from index 1 to the length of the list 

def scale( head: Node | None, factor: int) -> Node | None: # has head property and factor property
    if head is None:
        return None
    else: 
        return Node(head.value * factor, (scale(head.next,factor))) # returns Node w the head value and multiplies it by a factor, the nex node calls the function for recursion and had next head value and the factor


print(linkify([10, 20, 30, 40])) # why is this not wwoking -> down/ forgot the str method
print(scale(Node(10, Node(20, Node(30, None))), 2))   
print(max(Node(10, Node(20, Node(30, None)))))  
print(value_at(Node(10, Node(20, Node(30, None))), 0))  
