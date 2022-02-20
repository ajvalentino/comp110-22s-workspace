"""Exercist 5 Unit Testing."""

__author__ = "730466997"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Edge case test that tests an empty list."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_small_numbers() -> None:
    """Use case test that tests smaller numbers."""
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert only_evens(numbers) == [2, 4, 6, 8]


def test_only_evens_large_numbers() -> None:
    """Use case test that tests larger numbers."""
    numbers: list[int] = [42, 99, 130, 271]
    assert only_evens(numbers) == [42, 130]


def test_sub_negative_start_and_bigger_end() -> None:
    """Edge case test that tests when the start index is negative and when the end index is greater than the length."""
    numbers: list[int] = [-13, -4, 5, 10]
    assert sub(numbers, -1, 20) == [-13, -4, 5, 10]


def test_sub_small_numbers() -> None:
    """Use case test that tests smaller numbers."""
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(numbers, 2, 5) == [3, 4, 5]


def test_sub_large_numbers() -> None:
    """Use case test that tests larger numbers."""
    numbers: list[int] = [13, 26, 98, 145, 342, 832]
    assert sub(numbers, 1, 5) == [26, 98, 145, 342]


def test_concat_empty() -> None:
    """Edge case test that tests two empty lists."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []


def test_concat_small_numbers() -> None:
    """Use case test that tests two lists with small numbers."""
    first_list: list[int] = [1, 2, 3, 4]
    second_list: list[int] = [5, 6, 7, 8]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_large_numbers() -> None:
    """Use case test that tests two lists with large numbers."""
    first_list: list[int] = [392, 856]
    second_list: list[int] = [902, 234]
    assert concat(first_list, second_list) == [392, 856, 902, 234]