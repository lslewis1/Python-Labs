#10/8/14
#This program will keep a running total of the number of bugs collected duirng seven days
#The user inputs the number collected each day, and displays total when finished

i=1
sum=0
while i<=7:
    bugs=int(input("Please enter the total number of bugs for the day: "))
    i=i+1
total=(bugs*7)+10
print(total,"is the total number of bugs collected this week.")
