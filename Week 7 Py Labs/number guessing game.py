#10/15/14
#This program will run a number guessing game.
#The number is randomly generated, and user asked to guess a number

import random
x=random.randint (1,100)
g=int(input("Please enter your guess between 1 and 100 :"))
count=1
while g!=x:
    if g<x:
        print("Guess higher")
    else:
        print("Guess lower")
    count+=1
    g=int(input("Guess again :"))
print("You win, you guessed the number in", count, "tries")
