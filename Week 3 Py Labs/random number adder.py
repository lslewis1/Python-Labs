#9/17/14
#This program will import 2 random numbers
#The user will be asked to add the numbers
#The progam will also add the numbers and compare the answers

#x is one number
#y is the other number
#ans is the user input anser

import random
x=random.randint(1,100)
y=random.randint(1,100)
print(x,"+",y,"?")
ans=int(input("What is the answer? :"))
if (x+y==ans):
    print("Nice job")
else:
    print("You are incorrect, the correct answer is:", x+y)
