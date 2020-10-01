#10/1/14
#This program will ask a user to enter the weight of a package.
#The computer will then display the shipping charges.

#wp is the package weight
#sc is the shipping charge

wp=float(input("Enter the weight of the package in pounds :"))
if wp>10:
    sc=wp*3.80
elif wp>6:
    sc=wp*3.70
elif wp>2:
    sc=wp*2.20
else:
    sc=wp*1.10
print("The shipping charge is $", \
      format(sc, '.2f'))
