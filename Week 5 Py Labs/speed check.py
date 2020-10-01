#10/1/14
#This program will take an input speed and determine whether it is safe or not

#ts is travelling speed

ts=float(input("Please enter your travelling speed in mph :"))
if ts<25:
    print("Your travelling speed is below the interstate minimum.")
elif ts<=55:
    print("Your travelling speed is safe.")
else:
    print("Your travelling speed is not safe. Please slow down.")

    
