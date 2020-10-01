#9/29/14
#This program will play a game of rock paper scissors with the user

#c is the computer chosen number
#u is the user chosen input

import random
c=random.randint(1,3)
u=int(input("Please enter a 1 for scissors, 2 for rock, or a 3 for paper :"))
print("The computer chose",c)
if c==u:
    print("It is a tie")
elif (u==1 and c==3) or (u==2 and c==1) or (u==3 and c==2):
    print("You have won")
else:
    print("Computer wins")
