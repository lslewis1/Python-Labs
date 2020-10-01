#11/10/14

n=int(input("Enter the number of students: "))
names=[""]*n
grades=[0]*n
names[0]=input("Please enter the first student's name: ")
grades[0]=input("Please enter the first student's grade: ")
mx=grades[0]
mx_name=names[0]
for i in range(1,n):
    names[i]=input("Please enter the next student's name: ")
    grades[i]=input("Please enter the next student's grade: ")
    if grades[i]>mx:
        mx=grades[i]
        mx_name=names[i]
print("The student with the highest grade is", mx_name)
