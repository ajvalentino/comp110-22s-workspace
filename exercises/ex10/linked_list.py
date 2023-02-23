"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730466997"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    elif head.next is None:
        return head.data
    else:
        return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Returns the data of a Node at a given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.data
    else:
        return value_at(head.next, index - 1)


def max(head: Optional[Node], current_max: int = 0) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("Cannot call max with None")
    
    if head.next is None:
        if head.data > current_max:
            return head.data
        else:
            return current_max
    else:
        if head.data > current_max:
            return max(head.next, head.data)
        else:
            return max(head.next, current_max)


def linkify(items: list[int], new_node: Optional[Node] = None, i: int = 0) -> Optional[Node]:
    """Returns a Linked List of Nodes with the same values, in the same order, as the input list."""
    if len(items) == 0:
        return None
    elif new_node is None:
        i = len(items) - 1
        new_node = Node(items[i], None)
        return linkify(items, new_node, i - 1)
    elif i < 0:
        return new_node
    else:
        new_node = Node(items[i], new_node)
        return linkify(items, new_node, i - 1)


def scale(head: Optional[Node], factor: int, new_list: list[int] = []) -> Optional[Node]:
    """Return a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    if head is None:
        return None
    elif head.next is None:
        new_list.append(head.data * factor)
        return linkify(new_list)
    else:
        new_list.append(head.data * factor)
        return scale(head.next, factor, new_list)