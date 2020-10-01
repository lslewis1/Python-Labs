#9/17/14
#This program will calculate bonus pay for employees
#The bonus is 5% for over 40 hours of work
#The bonus is 4% otherwise

#hours is the variable for hours worked
#rate is the hourly pay rate
#pay is the hours times the rate
#Bonus is the bonus received

hours=float(input("Please enter the hours worked :"))
rate=float(input("Please enter the hourly pay rate :"))
pay=hours*rate
if hours>40:
    Bonus=pay*.05
    print("The bonus will be :","$",Bonus)
else:
    Bonus=pay*.04
    print("The bonus will be :","$",Bonus)
