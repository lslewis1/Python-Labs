#9/26/14
#This program will display a student's grade.
#The prgram will print a letter grade after receiving the numerical grade

#Grade is the numerical grade
#Letter is the letter grade

Grade=float(input("Please enter your numerical grade :"))
if Grade>=90:
    print("Your letter grade is an A.")
elif Grade>=80:
    print("Your letter grade is a B.")
elif Grade>=70:
    print("Your letter grade is a C.")
elif Grade>=60:
    print("Your letter grade is a D.")
else:
    print("Your letter grade is an F.")
    
