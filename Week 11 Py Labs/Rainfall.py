#11/10/14

sum=0
rf=[0]*12
rf[0]=int(input("Please enter the rainfall for the first month in inches: "))
highrf=rf[0]
lowrf=rf[0]
for x in range(1,12):
    rf[x]=int(input("Please enter the rainfall for the next month in inches: "))
    sum+=rf[x]
    if rf[x]>highrf:
        highrf=rf[x]
        hrfm=x
    if rf[x]<lowrf:
        lowrf=rf[x]
        lrfm=x
print("The total amount of rainfall for the year is: ",sum,"inches.")
avg=sum/12
print("The average monthly rainfall is: ",avg,"inches.")
print("The month with the highest rainfall is: ",highrf,"inches in month",hrfm)
print("The month with the lowest rainfall is: ",lowrf,"inches in month",lrfm)
    
