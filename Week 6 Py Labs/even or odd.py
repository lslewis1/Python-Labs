#10/6/14
#This program will take 10 input numbers and decide whether they are odd or even
#k is the variable controlling the while statement
#n is the user input number

k=1
while k<=10:
    n=int(input("Please enter your number :"))
    if n%2==0:
        print(n,"is even")
    else:
        print(n,"is odd")
    k=k+1
