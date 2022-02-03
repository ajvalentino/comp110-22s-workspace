"""EX03 - Wordle - The final evolution."""

__author__ = "730466997"

# declarations of named constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(secret: str, char: str) -> bool:
    """Checks if the given character is found in the secret word."""
    assert len(char) == 1
    
    somewhere = False
    checks = 0
    
    while not somewhere and checks < len(secret):
        if char == secret[checks]:
            return True
        else:
            checks = checks + 1
    
    return False


def emojified(guess: str, secret: str) -> str:
    """Changes guess to appropriate emojis depending on accuracy."""
    assert len(guess) == len(secret)
    
    # Declares needed variables
    checks = 0
    emojis: str = ""
    
    # Adds appropriate box
    while checks < len(secret):
        
        if guess[checks] == secret[checks]:
            emojis = emojis + GREEN_BOX
        elif contains_char(secret, guess[checks]):
            emojis = emojis + YELLOW_BOX
        else:
            emojis = emojis + WHITE_BOX
        
        checks = checks + 1
    
    return emojis


def input_guess(exp_length: int) -> str:
    """Asks for guess and determines if it is equal to the expected length."""
    guess: str = input(f"Enter a {exp_length} character word: ")
    
    # Checks word length and prompts user for new word until they match
    while len(guess) != exp_length:
        guess = input(f"That was not {exp_length} letters! Try again: ")
    
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turn: int = 1
    
    # Goes through each of the 6 turns
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        
        guess: str = input_guess(len(secret))
        
        print(emojified(guess, secret))

        if guess != secret and turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
        elif guess == secret:
            print(f"You won in {turn}/6 turns!")
            turn = 6

        turn += 1


# Allows me to run the program from the module
if __name__ == "__main__":
    main()