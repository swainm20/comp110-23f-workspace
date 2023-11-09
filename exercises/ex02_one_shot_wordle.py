"""EX02 - One Shot Wordle!"""
__author__ = "730578454"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guessed_letters: str = "" * len(secret)

guess_emoji: str = ""
result: str = ""
guessed_character = False
alt_idx: int = 0

idx: int = 0
if len(guess) != len(secret):   
    guess = (input("That was not 6 letters! Try again: "))
while idx < len(secret):
    if guess[idx] == secret[idx]:
        result += GREEN_BOX
        idx = idx + 1
    else:
        if alt_idx < len(secret) and guessed_character != True:
            if secret[alt_idx] == guess[idx]:
                guessed_character = True
                result += YELLOW_BOX
                alt_idx = alt_idx + 1
            else:
                result += WHITE_BOX
                alt_idx = alt_idx + 1
    print(result)
    print(guess_emoji)
if guess == secret:
    print("Woo! You got it!")
while guess != secret:
    if len(guess) == len(secret):
        if guess != secret:
            print("Not quite. Play again soon!")
            exit()       
    if guess == secret:
        print("Woo! You got it!")
