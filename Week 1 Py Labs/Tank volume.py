#9/5/14


#Assume we have to determine the volume of a cubical tank
#7.48 gallons of water fit in a cubic foot of space
#Determine the amount of water in gallons that will fill the tank

#s is the variable for a side of the tank
#g is the gallons of water needed
#v is the volume of the tank

s=float(input("Please enter the lenght of one edge of the tank in feet:"))
v=s*s*s
print("The volume of the tank is", v,"cubic feet:")
g=7.48*v
print("We will need", g,"gallons of water to fill the tank:")

    
