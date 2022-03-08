"""Test."""


def vowels_and_threes(string: str) -> str:
    i: int = 0
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    new_string: str = ""
    while i < len(string):
        if string[i] in vowels and i % 3 == 0:
            i += 1
        elif string[i] in vowels or i % 3 == 0:
            new_string += string[i]
            i += 1
        else:
            i += 1
    return new_string