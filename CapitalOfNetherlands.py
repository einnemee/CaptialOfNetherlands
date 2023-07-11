#What is the capital of The Netherlands?

capitalGuess = input("What is the capital of The Netherlands? ")
numberOfGuesses = 1

while capitalGuess != "Amsterdam":
    numberOfGuesses += +1
    capitalGuess = input("Guess again ")

print ("You guessed it. Amsterdam is the capital of The Netherlands")
print ("It took you", numberOfGuesses, "guesses.")
