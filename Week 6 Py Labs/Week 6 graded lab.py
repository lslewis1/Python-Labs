#10/10/14
#This program will calculate the total cost of a shopping trip.
#The user will input number of items purchased.
#A loop will be used to ask the cost of each item and calculate the sum of purchases.
#After calculating the sum, the sales tax at 6% is calculated.
#The program will display the cost of each item, the subtotal, sales tax, an total cost.

sum=0
count=1
ip=int(input("Please enter the number of items purchased: "))
while count<=ip:
    icost=float(input("Please enter the cost of the item: "))
    sum=sum+icost
    sub=sum
    count=count+1
print("sub-total: $",format(sub,'.2f'))
st=sub*.06
print("tax: $",format(st,'.2f'))
total=sub+st
print("total: $",format(total,'.2f'))

