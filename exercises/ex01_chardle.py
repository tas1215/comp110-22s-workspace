"""EX01 - Chardle - A cute toward Wordle."""

__author__ = "730312196"

enter_word: str = input("Enter a 5-Character word: ")

if len(enter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

enter_one_character: str = input("Enter a single character: ")

if len(enter_one_character) != 1:
    print("Error: Character must be a single character")
    exit()

num_match_character: int = 0

print("Searching for " + enter_one_character + " in " + enter_word)

if enter_one_character == enter_word[0]:
    print(enter_one_character + " found at index 0")
    num_match_character: int = num_match_character + 1

if enter_one_character == enter_word[1]:
    print(enter_one_character + " found at index 1")
    num_match_character: int = num_match_character + 1

if enter_one_character == enter_word[2]:
    print(enter_one_character + " found at index 2")
    num_match_character: int = num_match_character + 1

if enter_one_character == enter_word[3]:
    print(enter_one_character + " found at index 3")
    num_match_character: int = num_match_character + 1

if enter_one_character == enter_word[4]:
    print(enter_one_character + " found at index 4")
    num_match_character: int = num_match_character + 1

if num_match_character == 1:
    print(str(num_match_character) + " instance of " + enter_one_character + " found in " + enter_word)
else:
    if num_match_character > 0:
        print(str(num_match_character) + " instances of " + enter_one_character + " found in " + enter_word)
    else:
        print("No instances of " + enter_one_character + " found in " + enter_word)
