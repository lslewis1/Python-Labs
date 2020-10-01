#10/15/14
#This program will ask the user to enter a series of postivie numbers.
#Then the program will ask for a negative number to end the series.
#The program will add all of the positive numbers and display the sum

#x is the user input number

sum=0
print("Please enter a negative number when you wish to stop entering numbers.")
x=int(input("Please enter your number: "))
while x>=0:
    sum=sum+x
    x=int(input("Please enter your number: "))
    
print("The sum of your numbers is: ",sum)
        
