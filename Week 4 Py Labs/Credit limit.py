#9/22/14
#This program will determine whether one is going over their credit limit or not

#maxcred is the maximum credit limit
#npb is the not paid balance
#exp is the expenses for the current month

maxcred=float(input("Enter your maximum credit limit :"))
np=float(input("Enter the outstanding not paid balance :"))
exp=float(input("Enter your expenses for the current month :"))
if (np+exp)>maxcred:
    print("You are over your credit limit")
else:
    print("You are not over your limit")
