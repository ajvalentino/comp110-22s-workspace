"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730466997"

keyword: str = input("Enter a 5-character word: ")

if len(keyword) != 5:
    print("Error: Word must contain 5 characters")
    exit()

char: str = input("Enter a single character: ")

if len(char) != 1:
    print("Error: Character must be a single character.")
    exit()

instances: int = 0

print("Searching for " + char + " in " + keyword)

if keyword[0] == char:
    print(char + " found at index 0")
    instances = instances + 1

if keyword[1] == char:
    print(char + " found at index 1")
    instances = instances + 1

if keyword[2] == char:
    print(char + " found at index 2")
    instances = instances + 1

if keyword[3] == char:
    print(char + " found at index 3")
    instances = instances + 1

if keyword[4] == char:
    print(char + " found at index 4")
    instances = instances + 1

if instances == 0:
    print("No instances of " + char + " found in " + keyword)

if instances == 1:
    print(str(instances) + " instance of " + char + " found in " + keyword)

if instances > 1:
    print(str(instances) + " instances of " + char + " found in " + keyword)