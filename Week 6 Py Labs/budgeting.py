#10/8/14
#This program will take a user input of the amount budgeted for a month.
#A loop will prompt the user to enter each of the expenses for the month, and keep a total
#The program will display the amount the user is over of under budget.

budget=int(input("Please enter your budget for this month: "))
numExp=int(input("Please enter how many expenses you have: "))
count=1
sum=0
while count<=numExp:
    expense=int(input("Please enter your expense: "))
    sum=sum+expense
    count=count+1
if sum>budget:
    print("You are over your budget of", budget)
else:
    print("You are under your budget of", budget)
    
