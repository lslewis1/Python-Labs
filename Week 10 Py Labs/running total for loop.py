#11/5/14
#This for loop will ask the user to enter a number.
#The loop will run 10 times and display a running total of numbers entered.


sum=0
for x in range(1,10+1):
    x=int(input("Please enter your number: "))
    sum+=x
    print("sum =",sum)
print("goodbye!")
