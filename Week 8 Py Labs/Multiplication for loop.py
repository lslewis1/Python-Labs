#10/20/14
#This loop will display the multiplication table of a number entered by a user.
#The table will go up to 12 terms

x=int(input("Please enter the number for the multiplication table :"))
for n in range(1,13):
    product=x*n
    print(x,"x",n,"=", product)
        
