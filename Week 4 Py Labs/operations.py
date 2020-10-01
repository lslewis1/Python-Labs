#9/24/14
#This program will take two inputs of integers and perform an operation
#The integers will be divided, multiplied, subtracted, or added based on user input

#x is the first integer
#y is the second integer
#op is the operation
#ans is the answer to the operation

x=int(input("Please enter an integer number :"))
y=int(input("Please enter another integer :"))
op=int(input("Enter a 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division :"))
if op==1:
    ans=x+y
elif op==2:
    ans=x-y
elif op==3:
    ans=x*y
elif op==4:
    ans=x/y
else:
    ans= "wrong choice"
print("The answer to the operation is :", ans)
