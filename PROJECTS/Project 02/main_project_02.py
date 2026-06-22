from random import randint

def perfectGuess():
    # Computer does this
    guessNumber = randint(1, 100)
    # User guesses
    attempts = 0 # chances taken to guess
    while True:
        numberGuessed = int(input("Enter your guess value: ")) # number guessed by the user
        attempts += 1
        if numberGuessed == guessNumber:
            # guess += 1
            print("You guessed the number correctly!")
            print("The number is: ", guessNumber)
            break
        elif numberGuessed > guessNumber:
            # guess += 1
            print("Lower number please.")
        else:
            # guess += 1
            print("Higher number please.")
    return attempts


chances = perfectGuess()
print("The number of guesses: ", chances)