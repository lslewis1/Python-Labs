#9/17/14
#This program will ask a user to enter the exact amount of coins to make a dollar
#If the user correctly enters the amount of coins for a dollar, a message is displayed
#If not, the progam tells the usere if they were above or below a dollar

#p is the number of pennies
#n is the nickels
#d is dimes
#q is quarters

p=int(input("How many pennies are there? :"))
n=int(input("How many nickels are there? :"))
d=int(input("How many dimes are there? :"))
q=int(input("How many quarters are there? :"))
if ((p*1)+(n*5)+(d*10)+(q*25))==100:
    print("Congratulations, you have won the game")
else:
    if ((p*1)+(n*5)+(d*10)+(q*25))>100:
        print("You have more than a dollar")
    else:
        print("You have less than a dollar")
