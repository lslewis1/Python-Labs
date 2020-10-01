#11/5/14
#This program will ask the user to enter two numbers.
#The numbers will be added and sum displayed.
#The while loop will ask if they wish to do it again, it will repeat, otherwise terminate.

n1=int(input("Please enter your first number: "))
n2=int(input("Please enter your second number: "))
sum=n1+n2
print(n1,"+",n2,"=",sum)
run=int(input("Do you wish to continue? Enter 1 for yes. Enter 0 for no. : "))
while run==1:
    n1=int(input("Please enter your first number: "))
    n2=int(input("Please enter your second number: "))
    sum=n1+n2
    print(n1,"+",n2,"=",sum)
    run=int(input("Do you wish to continue? Enter 1 for yes. Enter 0 for no. : "))
