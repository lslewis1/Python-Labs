#11/14/14
#This program will ask for an input of number of students in the math class.
#Then each student's name will be entered, and the grade of the test.
#Names and grades will be stored in two different lists.
#The grades will be sorted from lowest to highest, with names in sync.
#The names of the students with the top threee grades will be displayed

n=int(input("Enter the number of students in the class: "))
names=[""]*n
grades=[0]*n
names[0]=input("Please enter the first student's name: ")
grades[0]=int(input("Please enter the first student's grade: "))
mx=grades[0]
mx_name=names[0]
for i in range(1,n):
    names[i]=input("Please enter the next student's name: ")
    grades[i]=int(input("Please enter the next student's grade: "))
for j in range(n-1,0,-1):
    for i in range(j):
        if grades[i]>grades[i+1]:
            tmp=grades[i]
            grades[i]=grades[i+1]
            grades[i+1]=tmp
            mx=tmp
            mx_name=names[i-1]
            mx2_name=names[i+1]
            mx3_name=names[i]
print("The students with the top 3 scores are: ")            
print(mx_name)
print(mx2_name)
print(mx3_name)
