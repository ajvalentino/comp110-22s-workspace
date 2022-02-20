"""Exercist 5, 'list' Utility Functions."""

__author__ = "730466997"


def only_evens(numbers: list[int]) -> list[int]:
    """Given a list of integers this function returns the even numbers."""
    even_numbers: list[int] = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def sub(numbers: list[int], start: int, end: int) -> list[int]:
    """Given a list and start/end indices this function returns a subset of the list."""
    sublist: list[int] = []
    i: int = 0
    for number in numbers:
        if i >= start and i < end:
            sublist.append(numbers[i])
        i += 1
    return sublist


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    """Given two lists this function concatenates them together."""
    concat_list: list[int] = []
    for number in first_list:
        concat_list.append(number)
    for number in second_list:
        concat_list.append(number)
    return concat_list