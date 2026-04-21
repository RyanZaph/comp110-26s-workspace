from __future__ import annotations

__author__ = "730472086"

class Node:

    value: int
    next: Node | None

def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next
    
    
def value_at(head: Node | None, index: int) -> int:
    if head is None: # checks if we reached the end of the listd
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0: # this is whtat we want so return value of node
        return head.value
    else:
        return value_at(head.next, index - 1) # not correct so we go back until we reach index 0  
    
print(value_at(Node(10, Node(20, Node(30, None))), 0))  

def max(head: Node | None):


#>>> from exercises.ex08.linked_list import Node, value_at
# >>> value_at(Node(10, Node(20, Node(30, None))), 0)
#10
#>>> value_at(Node(10, Node(20, Node(30, None))), 1)
#20
#>>> value_at(Node(10, Node(20, Node(30, None))), 2)
#30
#>>> value_at(Node(10, Node(20, Node(30, None))), 3)
# IndexError: Index is out of bounds on the list.

def __str__(self) -> str:
    if self.next is None:
        return f"{self.value} -> None"
    else:
        return f"{self.value} -> {self.next}"


Courses: Node = Node(110, Node(210, None))
print(Courses)
head: Node = Node(
    110, None
)  # Now that we are not in the Node Class it'self', we refer to the instacne of the node class using the name of the variable we assign it to.


def sum(head: Node | None) -> int:
    # base case
    if head.next is None:
        return head.value
    # recursion rule
    else:
        return sum(head.next) + head.value  # next nodes sum + my value


# Integration Create the ndes from the slides
node_c: Node = Node(4, None)
node_b: Node = Node(0, node_c)
node_a: Node = Node(5, node_b)


print(node_a.value)
# value of node_b remember node_b isb node_a.next)

print(node_a.next.value)
# Value od node_c | remember node is bide_b.next or node_a.next.next
print(node_b.next.value)  # of node_b.next.next.value


def __str__(self) -> str:
    if self.next is None:
        return f"{self.value} -> None"
    else:
        return f"{self.value} -> {self.next}"


Courses: Node = Node(110, Node(210, None))
print(Courses)