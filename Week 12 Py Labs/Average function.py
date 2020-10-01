#11/19/14

import list_functions
n=int(input("How many numbers would you like to average? "))
num=[0]*n
for i in range(n):
    num[i]=int(input("Please enter a number: "))
avg=list_functions.average(num)
print("The average of the list is:",avg)
