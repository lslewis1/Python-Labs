#9/8/14
#Write a program to determine the take home pay for employees of a company
#inputs are hr(hourly rate) and hw(hours worked)
#gs is the gross salary
#deduct 10.55% from the total to display take home
#th is the variable for take home pay after deductions

hr=float(input("Please enter your hourly rate in dollars:"))
hw=float(input("Please enter the number of hours worked:"))
gs=hw*hr
th=gs-(gs*.1055)
print("Your take home income is: $", th)

