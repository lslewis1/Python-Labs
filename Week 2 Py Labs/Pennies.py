#9/10/14
#This program will determine the amount of quarters, dimes, nickels, and pennies one would receive
#The amount of coins receive is based on how many pennies are given as an input

#tp is total pennies started with
#p is pennies
#q is quarters
#d is dimes
#n is nickels

tp=int(input("Please enter the total amount of pennies you have:"))
q=tp//25
d=(tp-(q*25))//10
n=(tp-((d*10)+(q*25)))//5
p=(tp-((n*5)+(d*10)+(q*25)))//1
print("You will have", q,"quarters", d,"dimes", n,"nickels, and", p,"pennies")























