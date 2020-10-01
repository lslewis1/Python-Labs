#9/15/14
#This program calculates gross pay for employees that work overtime with a 5% bonus to the salary

#hrs is hours worked
#rate is the pay rate
#gross is the gross pay

hrs=float(input("Please enter your hours worked :"))
rate=float(input("Please enter your hourly pay rate :"))
gross=hrs*rate
if hrs>50:
    gross=gross*1.05
print("The total take home pay is: $", gross)
