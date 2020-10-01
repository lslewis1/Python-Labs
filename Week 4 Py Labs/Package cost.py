#9/24/14
#This program will take an input of packages and display discount and total amount.
#The total amount of purchase is after the discount

#np is the number of packages
#d is the discount
#total is the price without discount
#cost is the cost paid with discount

np=int(input("Please enter amount of packages purchased :"))
if np>=100:
    d=0.5
elif np>=50:
    d=0.4
elif np>=20:
    d=0.3
elif np>=10:
    d=0.2
else:
    d=0
total=(np*99)
d=99*d*np
cost=total-d
print("The discount is :$",d)
print("The cost to pay is :$", cost)
        
