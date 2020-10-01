#10/20/14
#This program will utilize a for loop to convert a given temperature.
#The conversion will be between celsius and fahrenheit based on user input.

ch=int(input("Enter a 1 for celsuis to fahrenheit, or a 2 for fahrenheit to celsius: "))
if ch==1:
    start=int(input("Please enter your start value: "))
    end=int(input("Please enter your end value: "))
    step=int(input("Please enter what you want to count by: "))
    for temp in range(start,end+1,step):
        F=(9/5*temp)+32
        print(temp,"degrees Celsius =",format(F,'.2f'),"degrees Fahrenheit.")
elif ch==2:
    start=int(input("Please enter your start value: "))
    end=int(input("Please enter your end value: "))
    step=int(input("Please enter what you want to count by: "))
    for temp in range(start,end+1,step):
        F=(temp-32)*(5/9)
        print(temp,"degrees Fahrenheit =",format(F,'.2f'),"degrees Celsius.")
