from math import *
import random
from random import randint
x=random.randint(0,9)
counter=0
while True:
    guess=input("Type a number between 0 and 9, or 'exit' please:")

    try:
        if guess == 'exit':
            break

        intGuess = int(guess)
        if intGuess>9 or intGuess<0:
            print ("Not in range, guess again")
            continue

        counter+=1
        if intGuess==x:
            print("You guessed right in %s tries." % str(counter))
            break
        elif intGuess<x:
            print("You guessed too low")
        elif intGuess>x:
            print("You guessed too high")

    except ValueError:
        print("Bad input")





