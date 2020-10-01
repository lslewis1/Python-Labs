#10/20/14
#This program will take a list of numbers and determine the max number.
#It will also determine the position of this number in the list.

location=1
num=int(input("Please enter how many numbers have in the list: "))
max=int(input("What is the first number in the list? "))
for n in range(num-1):
    x=int(input("Please enter the next number :"))
    if x>max:
        max=x
        location=n+2
print("The maximum number on your list is: ", max,", at number", location,"on your list.")
