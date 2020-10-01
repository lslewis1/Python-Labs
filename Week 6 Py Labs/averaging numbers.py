#10/8/14
#This program will ask a user to input how many numbers they want averaged.
#The loop will ask the user for each of the numbers and calculate the average.

n=int(input("How many numbers would you like to average? "))
i=1
sum=0
while i<=n:
    x=int(input("Enter your number: "))
    sum=sum+x
    i=i+1
average=sum/n
print("The average of your", n,"numbers is:", average)
