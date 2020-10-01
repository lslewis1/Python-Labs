#10/6/14
#This program will ask for the speed of a vehicle in mph, and hours traveled.
#Then a loop will be used to display the distance traveled for each hour.
#distance= speed x time

#sp is the speed in mph
#ht is the hours traveled
#d is the distance traveled in miles
#i is the control for the loop

sp=int(input("Please enter the speed of the vehicle in mph :"))
ht=int(input("Please enter the hours traveled as a whole number :"))
i=1
while i<=ht:
    d=sp*i
    print("In",i,"hours, the vehicle traveled",d,"miles.")
    i=i+1


