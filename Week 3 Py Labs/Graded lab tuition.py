#9/19/14
#This program will deterimine the total charges for one semester of college
#This total will include tuition costs as well as other fees.

#hours is the enrollment hours
#cps is comuter science fees
#otr is other major fees
#res is the residential status
#tuition is the tuition based on hours
#lf is the lab fee
#total is the total cost of attendance

hours=int(input("Please enter the number of hours you are planning to enroll for :"))
cps=int(input("Please enter a 1 if you are a CS major, or a 2 otherwise :"))
res=int(input("Please enter a 1 if you are an in-state student, or a 2 otherwise :"))
if hours<12:
    tuition=225*hours
else:
    tuition=2640
if cps==1:
    lf=100
else:
    lf=75
if res==2:
    tuition=tuition*1.15
total=(tuition+lf)
print("Your total cost of attendance will be $", total)



