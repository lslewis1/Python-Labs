#10/6/14
#This program will use a loop to display the number of calories burned after time.
#The times are: 10,15,20,25, and 30 minutes

#i controls the while loop
#cb is calories burned
#m is minutes

i=10
while i<=30:
    m=i
    cb=m*3.9
    i=i+5
    print(cb,"Calories burned for running for", m,"minutes.")
