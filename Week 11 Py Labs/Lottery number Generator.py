#11/10/14

lnumber=[0]*7
import random
print("The lottery number is: ")
for x in range(7):
    lnumber[x]=random.randint(0,9)
    print(lnumber[x],end='')   
