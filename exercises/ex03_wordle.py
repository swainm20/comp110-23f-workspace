"""EX03 - Structured Wordle!"""
__author__ = "730578454"
"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8" """

"""guessed_letters: str = "" * len(secret)

guess_emoji: str = ""
result: str = ""
guessed_character = False
alt_idx: int = 0"""

character: str = input("Guess a single character: ")
search_string: str = input("Write a secret word: ")

idx: int = 0
def contains_char(search_string, character):
    """Returns character when found in a idx of search_string."""
    assert len(character) == 1
    if character in search_string:
        return True
    else:
        return False 
result = contains_char(search_string, character)

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

def emojified(guess, secret):
    """Returns """
        if secret[alt_idx] == guess[idx]:

    assert len(emojified) == len(search_string)




""" idx: int = 0
while result == True:
    if alt_idx < len(secret) and guessed_character != True:
        if secret[alt_idx] == guess[idx]:
                guessed_character = True
                result += YELLOW_BOX
                alt_idx = alt_idx + 1
               
        else:
                result += WHITE_BOX
                alt_idx = alt_idx + 1

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
        print("Woo! You got it!") """