#9/29/14
#This program will take three random integers and see if the first is divisible
#It will check if the first is divisible by the other two or not

#n1 is the first integer
#n2 is the second integer
#n3 is the third integer

import random
n1=random.randint(1,100)
n2=random.randint(1,100)
n3=random.randint(1,100)
if (n1%n2==0) and (n1%n3==0):
    print(n1,"is divisible by",n2,"and",n3)
elif (n1%n2==0) and (n1%n3!=0):
    print(n1,"is divisible by",n2,"but not by",n3)
elif (n1%n2!=0) and (n1%n3==0):
    print(n1,"is not divisible by",n2,"But is is divisible by",n3)
else:
    print(n1,"is not divisible by",n2,"or",n3)
