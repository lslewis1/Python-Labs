#9/22/14
#This program will determine average number of calories that should be consumed.
#The calories are based on gender and weight

#gend is the gender
#wt is the weight input
#cal is the calories to be consumed

gend=int(input("Enter a 1 if you are a male, or a 2 if you are female:"))
wt=float(input("Please enter your weight in pounds:"))
if gend==1:
    cal=18*wt
else:
    cal=15*wt
print("The daily average number of calories you should consume is", cal, "Calories")
