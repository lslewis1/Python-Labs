#10/1/14
#This program will determine a person's BMI
#Then it will display wheter the person in optimal weight, over, or under

#bmi is the body mass indicator
#w is the weight
#h is the height

w=float(input("Enter your weight in pounds :"))
h=float(input("Enter your height in inches :"))
bmi=(w*703)/(h*h)
print("Your body mass indicator is", \
      format(bmi, '.2f'))
if bmi>25:
    print("You are overweight.")
elif bmi>=18.5:
    print("Your weight is optimal.")
else:
    print("You are underweight.")
