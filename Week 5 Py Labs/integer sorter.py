#9/29/14
#This program will sort three integers from least to greatest.

#x is the first integer
#y is the second integer
#z is the third integer

x=int(input("Please enter an integer number :"))
y=int(input("Please enter another integer number :"))
z=int(input("Please enter another integer number :"))
if (x>y) and (y>z):
    print(z,y,x)
elif (x>z) and (z>y):
    print(y,z,x)
elif (x>y) and (z>x):
    print(y,x,z)
elif (x>z) and (x>y):
    print(z,x,y)
elif (y>x) and (z>y):
    print(x,y,z)
else:
    print(x,z,y)
    
