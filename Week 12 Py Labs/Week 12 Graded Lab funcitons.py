#11/21/14
#This program will take an input of five test scores.
#Two fucntions will be used to display the letter grade of the scores, and
#The overall average
#A list will be used for the test scores in the calc_average function

def calc_average(mylist):
    sum=0
    for i in range(len(mylist)):
        sum+=mylist[i]
    average=sum/(len(mylist))
    return average
def determine_grade(a):
    if a>=90:
        grade="A"
    elif a>=80:
        grade="B"
    elif a>=70:
        grade="C"
    elif a>=60:
        grade="D"
    else:
        grade="F"
    return grade

gradelist=[0]*5
for x in range(5):
    gradelist[x]=int(input("Please enter a grade: "))
    grade=determine_grade(gradelist[x])
    average=calc_average(gradelist)
for y in range(5):
    grade=determine_grade(gradelist[y])
    print(gradelist[y],"-",grade)
grade=determine_grade(average)
print("Average is: ",average,"-",grade)

