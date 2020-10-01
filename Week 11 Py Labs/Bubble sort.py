#11/12/14
#This is a bubble sort program, that asks the user for ten numbers.
#The program prints the numbers in a list, then sorts them.

num=[0]*10
for i in range(10):
    num[i]=int(input("Please enter a number: "))
print("Before the bubble sort:")
print(num)
print("After the bubble sort:")
for j in range(9,0,-1):
    for i in range(j):
        if num[i]>num[i+1]:
            tmp=num[i]
            num[i]=num[i+1]
            num[i+1]=tmp
print(num)
        
