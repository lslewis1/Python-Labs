#9/3/14

#Assume we have to paint a wall with a window.
#We know that a gallon of paint covers 4.56 square feet area.
#Determin the amount of paint needed to paint the whole wall.

#l is the variable to store lenght of the wall
#h is the variable to store height fo the wall
#lw is the variable ot store length of the window
#hw is the variable to store height of the window
#g is the number of gallons used

l=float(input("Please enter the length of the wall:"))
h=float(input("Please enter the height of the wall:"))
lw=float(input("Please enter the lenght of the window:"))
hw=float(input("Please enter the height of the window:"))
ap=(l*h)-(lw*hw)
g=ap/4.56
print("The amount of paint needed to paint the whole wall is",g,"gallons")
