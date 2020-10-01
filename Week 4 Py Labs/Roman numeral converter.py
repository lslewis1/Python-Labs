#9/22/14
#This program will convert numbers between 1-10 into roman numerals
#If the range is exceeded, an error message is displayed

#num is the number entered (1-10)

num=int(input("Please enter an integer between 1 and 10 :"))
if num>10:
    print("sorry you have entered an incorrect number")
if num==1:
    print("I")
elif num==2:
    print("II")
elif num==3:
    print("III")
elif num==4:
    print("IV")
elif num==5:
    print("V")
elif num==6:
    print("VI")
elif num==7:
    print("VII")
elif num==8:
    print("VIII")
elif num==9:
    print("IX")
elif num==10:
    print("X")
