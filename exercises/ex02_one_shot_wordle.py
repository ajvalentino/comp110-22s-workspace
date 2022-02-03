"""EX02 - One-Shot Wordle - Another cute step towards Wordle."""

__author__ = "730466997"

# declarations of named constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# declarations of initial variables
secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
i: int = 0
checks: int = 0
result: str = ""

# checks the length of the guess
while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

# checks each character of the guess
while i < len(secret):
    if guess[i] == secret[i]:
        result = result + GREEN_BOX
    else:
        somewhere: bool = False
        
        # checks if the character is present elsewhere in the code
        while not somewhere and checks < len(secret):
            if guess[i] == secret[checks]:
                somewhere = True
            else:
                checks = checks + 1
        
        # determines whether a yellow or green box is appropriate
        if somewhere:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    
    # resets checks and moves on to next character
    checks = 0
    i = i + 1

# prints emoji results
print(result)

# prints final confirmation of success or failure
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")