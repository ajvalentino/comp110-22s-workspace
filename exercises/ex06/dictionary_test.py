"""Unit testing the dictionaries file."""

__author__ = "730466997"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """Edge case test that tests an empty dicitonary."""
    dictionary = {}
    assert invert(dictionary) == {}


def test_invert_names() -> None:
    """Use case test that tests first names and last names."""
    dictionary = {
        "AJ": "Valentino",
        "Charlie": "Armstrong",
        "Jacob": "Ewoldt",
        "Jackson": "Handy"
    }
    assert invert(dictionary) == {
        "Valentino": "AJ",
        "Armstrong": "Charlie",
        "Ewoldt": "Jacob",
        "Handy": "Jackson"
    }


def test_invert_abbreviations() -> None:
    """Use case test that tests schools and their abbreviations."""
    dictionary = {
        "UNC": "University of North Carolina at Chapel Hill",
        "NYU": "New York University",
        "OSU": "Ohio State University",
        "ECU": "East Carolina University"
    }
    assert invert(dictionary) == {
        "University of North Carolina at Chapel Hill": "UNC",
        "New York University": "NYU",
        "Ohio State University": "OSU",
        "East Carolina University": "ECU"
    }


with pytest.raises(KeyError):
    dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(dictionary)


def test_favorite_color_empty() -> None:
    """Edge case test that tests an empty dictionary."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_favorite_color_no_tie() -> None:
    """Use case test that tests a dictionary with one favorite color."""
    dictionary: dict[str, str] = {
        "AJ": "Green",
        "Charlie": "Green",
        "Jacob": "Blue",
        "Jackson": "Purple",
        "Carson": "Red",
        "Daphne": "Pink",
        "Daniel": "Green",
        "Sam": "Blue"
    }
    assert favorite_color(dictionary) == "Green"


def test_favorite_color_tie() -> None:
    """Use case test that tests a dictionary with a tie between colors."""
    dictionary: dict[str, str] = {
        "AJ": "Green",
        "Charlie": "Green",
        "Jacob": "Blue",
        "Jackson": "Purple",
        "Carson": "Red",
        "Daphne": "Pink",
        "Daniel": "Green",
        "Sam": "Blue",
        "Christina": "Blue"
    }
    assert favorite_color(dictionary) == "Green"


def test_counts_empty() -> None:
    """Edge case test that tests an empty list."""
    strings: list[str] = []
    assert count(strings) == {}


def test_counts_names() -> None:
    """Use case test that tests names."""
    strings: list[str] = ["Anthony", "Anthony", "John", "John", "John", "Austin", "Valentino", "Valentino"]
    assert count(strings) == {
        "Anthony": 2,
        "John": 3,
        "Austin": 1,
        "Valentino": 2
    }


def test_counts_colors() -> None:
    """Use case test that tests colors."""
    strings: list[str] = ["Blue", "Green", "Red", "Blue", "Red", "Blue"]
    assert count(strings) == {
        "Blue": 3,
        "Green": 1,
        "Red": 2
    }