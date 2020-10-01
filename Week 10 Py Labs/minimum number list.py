#11/3/14

index=int(input("How many numbers do you wnat in the list?"))
y=[0]*index
y[0]=int(input("Please enter the first number: "))
min=y[0]
for x in range(1,index):
    y[x]=int(input("Please enter another number for the list: "))
    if y[x]<min:
         min=y[x]
print("The minimum number in the list is: ",min)
    

    
