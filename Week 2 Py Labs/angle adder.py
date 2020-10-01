#9/10/14
#This program will display the sum of two angles in terms of circles, degrees, minutes, and seconds
#60 secs is a minute
#60 mins is a degree
#360 degrees is a circle

#a1 is angle 1
#a2 ia angle 2
#c is circles
#s is seconds
#d is degrees
#m is minutes
#at is the sum of the angles

da1=int(input("Please enter first angle in degrees"))
ma1=int(input("Please enter first angle in minutes"))
sa1=int(input("Please enter first angle in seconds"))
ma1=sa1//60
sa1=sa1%60
da1=ma1//60
da1=da1%60
ca1=da1//360
ca1=ca1%360
a1=(sa1+ma1+da1)


da2=int(input("Please enter first angle in degrees"))
ma2=int(input("Please enter first angle in minutes"))
sa2=int(input("Please enter first angle in seconds"))
ma2=sa2//60
sa2=sa2%60
da2=ma2//60
da2=da2%60
ca2=da2//360
ca2=ca2%360
a2=(sa2+ma2+da2)

at=a1+a2
print("The sum of the two angles will be",

