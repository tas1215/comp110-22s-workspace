"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of an number between 1-5, what is it?")
guess: int = int(input("What is your guess? ")) 

if guess == SECRET: 
    print("You guessed correctly!!")
    print("have a wonderful day")
else:
    print("sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("you guessed to high")
    else:
        print("you guessed to low")

print("Game over.")