"""Exercising the use of our newly learned topic: dictionaries."""

__author__ = "730466997"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of dictionaries."""
    # Declare return value
    inverted: dict[str, str] = dict()
    
    # Invert each key and value
    for key in dictionary:
        if dictionary[key] in inverted:
            raise KeyError("KeyError")
        inverted[dictionary[key]] = key

    # Return inverted list
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most frequent color in a dictionary of names and favorite colors."""
    # Declare counter, return variable, and list of colors
    i: int = 0
    favorite: str = ""
    colors: list[str] = []

    # Create a list of the colors
    for key in dictionary:
        colors.append(dictionary[key])
    
    # Compare the count of each value to each other
    for color in colors:
        if colors.count(color) > i:
            i = colors.count(color)
            favorite = color

    # Return most frequent color
    return favorite


def count(strings: list[str]) -> dict[str, int]:
    """Creates a dictionary of the count of each value in a list."""
    # Declare return value
    counts: dict[str, int] = dict()

    # Count each value
    for item in strings:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    # Return dictionary of counts
    return counts