#What is the capital of The Netherlands?

capitalGuess = input("What is the capital of The Netherlands? ").upper()
numberOfGuesses = 1

while capitalGuess != "AMSTERDAM":
    numberOfGuesses += +1
    if numberOfGuesses > 3:
        print("You guessed incorrectly three times. Game over.")
        break
    capitalGuess = input("Guess again ")

if capitalGuess == "AMSTERDAM":
    print ("You guessed it. Amsterdam is the capital of The Netherlands. It took you ", numberOfGuesses, " guesses.")
