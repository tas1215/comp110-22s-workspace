"""One Shot Wordle."""

___author___ = "730312196"

# this is the secret word
secret: str = "python"

# emoji codes for the boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


# loop varibles and user input varibles
i = 0

result: str = ""

chr_exists = False

num_alt_indi = 0

# ask the user what word they want to guess. 
enter_word: str = input(f"What is your {len(secret)}-letter guess? ")

# loop to check if the entered guess is the correct amount of letters
while len(enter_word) != len(secret):
    enter_word = input(f"That was not {len(secret)} letters! Try again: ")
# loop for checking each indice for a match. If the indice is less than the length of the word then run through the loop. Once i  > length of secret then stop loop
while i < len(secret):
    # add green box to result if true
    if secret[i] == enter_word[i]:
        result = result + GREEN_BOX
    else:
        # if the letter does not match, determine if the letter is in the word. 
        while num_alt_indi < len(secret):
            if enter_word[i] == secret[num_alt_indi]:
                chr_exists = True
            num_alt_indi = num_alt_indi + 1
            # add yellow box to result if true
        if chr_exists:
            result = result + YELLOW_BOX
            # add white box to result if not true
        else:
            result = result + WHITE_BOX
    # add indice to check next character and reset values of alt indicies and bool so that code will not be continuous
    i = i + 1
    num_alt_indi = 0
    chr_exists = False
# print the colored boxes that cooresponds with guessed word
print(result)

# print the overall ending of the guess of the word
if enter_word == secret:
    print("Woo! You got it!")
else: 
    print("Not Quite. Play again soon!")