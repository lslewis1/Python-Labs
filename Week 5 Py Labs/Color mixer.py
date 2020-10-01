#9/29/14
#This program will take three user entered primary colors and display the color made when mixed

#c1 is the first color
#c2 is the second color
#mix is the color made when mixed

c1=int(input("Choose 1 for red, 2 for blue, or a 3 for yellow :"))
c2=int(input("Choose 1 for red, 2 for blue, or a 3 for yellow :"))
if (c1==1 and c2==2)or (c2==1 and c1==2):
    mix="Purple"
elif (c1==1 and c2==3) or (c2==1 and c1==3):
    mix="Orange"
elif (c1==2 and c2==3) or (c2==2 and c1==3):
    mix="Green"
else:
    mix="You did not choose from the correct colors"
print(mix)
