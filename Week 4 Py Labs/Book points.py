#9/24/14
#This program will determine the number of points a person receives based on books purchased

#books is the number of books purchased
#points is the points received

books=int(input("Please enter the number of books you have purchased :"))
if books==0:
    points=0
elif books==1:
    points=5
elif books==2:
    points=15
elif books==3:
    points=30
else:
    points=60
print("You have received", points,"Points")
