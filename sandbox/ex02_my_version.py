"""EX01 - One-Shot Wordle - Another cute step towards Wordle."""

__author__ = "730466997"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret: str = "knoll"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
i: int = 0
checks: int = 0
somewhere: bool = False
result: str = ""

while len(guess) != len(secret):
    guess = input(f"That was not {len(secret)} letters! Try again: ")

while i < len(secret):
    if guess[i] == secret[i]:
        result = result + GREEN_BOX
        somewhere = True
    else:
        while checks < len(secret):
            if guess[i] == secret[checks]:
                result = result + YELLOW_BOX
                somewhere = True
                checks = len(secret)
            checks = checks + 1
        
        checks = 0
    
    if not somewhere:
        result = result + WHITE_BOX
    
    i = i + 1
    somewhere = False

print(result)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")