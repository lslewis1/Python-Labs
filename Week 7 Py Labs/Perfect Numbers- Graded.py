#10/17/14
#This program will determine whether an integer is perfect or not.
#It is perfect if the sum of its factors is equal to itself.

sum=0
x=int(input("Please enter an integer number to see if it is perfect :"))
div=1
while div<=x//2:
    if x%div==0:
        sum=sum+div
    div+=1
if sum==x:
    print(x,"Is a perfect number.")
else:
    print(x,"Is not a perfect number.")

    
