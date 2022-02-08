"""Wordle for exercise 3."""

__author__ = "730312196"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(the_word: str, single_letter: str) -> bool:
    """This function searches for a specific letter in the guessed word."""
    assert len(single_letter) == 1
    i: int = 0
    while i < len(the_word):
        if the_word[i] == single_letter:
            return True
        else:
            i += 1
    return False


def emojified(the_word: str, secret: str) -> str:
    """This will check each letter and then print emoji boxes."""
    assert len(the_word) == len(secret)
    i: int = 0
    result: str = ""
    while i < len(secret):
        if the_word[i] == secret[i]:
            result += GREEN_BOX
        else: 
            if contains_char(secret, the_word[i]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result


def input_guess(the_word: int) -> str:
    """This function will ask the player to make a guess at the correct length."""
    the_guess: str = input(f"Enter a {the_word} character word: ")
    while len(the_guess) != the_word:
        the_guess = input(f"That wasn't {the_word} chars! Try again: ")
    return the_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    i: int = 1
    secret: str = "codes"
    the_guess: str = ""
    while i < 7:
        print(f"=== Turn {i}/6 ===")
        the_guess = input_guess(len(secret))
        print(emojified(the_guess, secret))
        if the_guess == secret:
            print(f"You won in {i}/6 turns!")
            i += 7
        if the_guess != secret:
            i += 1
    if the_guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()