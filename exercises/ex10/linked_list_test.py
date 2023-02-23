"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale

__author__ = "Your PID"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Value at of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)

    
def test_value_at_non_empty() -> None:
    """Index above 0 of a non-empty list should return the data value of that index."""
    linked_list = Node(1, Node(2, Node(3, Node(4, None))))
    assert value_at(linked_list, 2) == 3


def test_max_empty() -> None:
    """Max of an empty list should return a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_max_single() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(3, None)
    assert max(linked_list) == 3


def test_max_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(4, Node(3, None))))
    assert max(linked_list) == 4


def test_linkify_one_int() -> None:
    """Linkify with one int in list should return int -> None."""
    normal_list = [4]
    assert is_equal(linkify(normal_list), Node(4, None))


def test_linkify_multiple_ints() -> None:
    """Linkify with one int in list should return int -> None."""
    normal_list = [4, 5, 6, 7]
    assert is_equal(linkify(normal_list), Node(4, Node(5, Node(6, Node(7, None)))))


def test_scale_empty() -> None:
    """Scale of an empty list should return a Value Error."""
    assert scale(None, 2) is None


def test_scale_by_three() -> None:
    """Scale with a factor of three should return a linked list factored by three."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(scale(linked_list, 3), Node(3, Node(6, Node(9, None))))