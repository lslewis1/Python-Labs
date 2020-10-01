#9/10/14
#This program will display the sum of two angles in terms of circles, degrees, minutes, and seconds
#60 secs is a minute
#60 mins is a degree
#360 degrees is a circle

#c is circles
#s is seconds
#s1 and s2 for the two angles
#d is degrees
#d1 and d2 for the two angles
#m is minutes
#m1 and m2 for the two angles
#st for total seconds
#mt for total minutes
#dt for total degrees
#m3 for left over minutes

d1=int(input("Please type in the degrees of the first angle:"))
d2=int(input("Please type in the degrees of the second angle:"))
m1=int(input("Please type in the minutes of the first angle:"))
m2=int(input("Please type in the minutes of the second angle:"))
s1=int(input("Please type in the seconds of the first angle:"))
s2=int(input("Please type in the seconds of the second angle:"))

m3=(s1+s2)//60
st=(s1+s2)%60
d3=(m1+m2+m3)//60
mt=(m1+m2+m3)%60
c=(d1+d2+d3)//360
dt=(d1+d2+d3)%360

print("The sum of the two angles results in:", c,"circles,", dt,"degrees,", mt,"minutes, and", st,"seconds.")
