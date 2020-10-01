#11/5/14
#This program uses a while loop to let a user enter a number.
#The number will be multiplied by 10 and assigned to the PRODUCT variable.
#Loop will run as long as PRODUCT is less than 100. Then says "goodbye".

num=int(input("Please enter your number: "))
PRODUCT=num*10
while PRODUCT<100:
    num=int(input("Please enter your number: "))
    PRODUCT=num*10
print("goodbye")
