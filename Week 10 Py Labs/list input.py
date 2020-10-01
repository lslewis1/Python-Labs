#11/3/14
#This program will ask a user to input a list of numbers.
#The program will then display the list of numbers.

index=int(input("How many numbers do you wnat in the list?"))
y=[0]*index
for x in range(index):
    y[x]=int(input("Please enter a number for the list: "))
print("The numbers in the list are: ")
for a in range(index):
    print(y[a])
    
