#9/17/14
#This program will calculate "magic dates"
#a month in numeric form will be entered
#a day
#and a two digit year
#The program will determine if the month times the day equals the year

#month is the numeric month
#day is the numeric day
#year is the two digit year

month=int(input("Please enter a numeric month :"))
day=int(input("Please enter a numeric day :"))
year=int(input("Please enter a two digit year :"))
if (month*day)==year:
    print("The date you have entered is magic")
else:
    print("The date is not magic")
    
