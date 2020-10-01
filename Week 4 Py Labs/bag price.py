#9/24/14
#This progam will take an input of a number of birdfeed bags.
#It will then determine the total cost based on the number purchased

#bags is bags purchased
#price is total price payed

bags=int(input("Please give a number of bags to purchase :"))
if bags>=75:
    price=bags*1.50
elif bags>=65:
    price=bags*1.70
elif bags>=55:
    price=bags*1.90
else:
    price=bags*2.15
print("The total price will be :$", price)
