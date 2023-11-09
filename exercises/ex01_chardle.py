"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730578454"
    
word_1: str = input("Please enter a 5-character word. ")

if len(word_1) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character_1: str = input("Please enter a single character. ")

if len(character_1) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + character_1 + " in " + word_1)

character_idx: int = 0

if word_1[0] == character_1:
    print(character_1 + " found at index 0")
    character_idx += 1

if word_1[1] == character_1:
    print(character_1 + " found at index 1")
    character_idx += 1

if word_1[2] == character_1:
    print(character_1 + " found at index 2")
    character_idx += 1
    
if word_1[3] == character_1:
    print(character_1 + " found at index 3")
    character_idx += 1

if word_1[4] == character_1:
    print(character_1 + " found at index 4")
    character_idx += 1

if character_idx > 1: 
    print(f"{character_idx}" + " instances of " + character_1 + " found in " + word_1)

if character_idx == 1:
    print(f"{character_idx}" + " instance of " + character_1 + " found in " + word_1)

if character_idx == 0:
    print(" No instances of " + character_1 + " found in " + word_1)