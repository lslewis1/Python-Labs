#9/15/14
#This program will determine the gross pay for an employee of a company.
#the hourly rate is $10
#if an employee works more than 20 hours there is a $5 extra for each hour.

#hrs is the hours worked
#gross is the gross pay
#othrs is overtime hours
#otpay is overtime pay

hrs=float(input("Please enter the hours worked:"))
gross=10*hrs
if hrs>20:
    othrs=hrs-20
    otpay=othrs*5
    gross=(gross+otpay)
print("The take home pay will be: $",gross)
