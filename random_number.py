#random number guessing game
from random import randint
number = randint(1, 10)
#inital number of guesses (obvisouly 0)
guesses_taken = 0
#loops through the guesses
while guesses_taken < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    guesses_taken += 1
    if guess < number:
        print("Your guess is too low." )
    if guess > number:
        print("Your guess is too high.")
    if guess == number:
        break
#provides final feedback
if guess == number:
    print("Congratulations! You guessed correctly!")
if guess != number:
    print("Better luck next time. The number was " + str(number))