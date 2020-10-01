#10/1/14
#This program will take a user input of a number of seconds.
#The program will then display how many full minutes, hours, days, and leftover seconds there are

#ts is the input of seconds
#s1 is the leftover seconds for the minutes
#s2 is the seconds for hours
#s3 is the seconds for days
#m is the number of minutes
#h is the number of hours
#d is the number of days

ts=int(input("Enter the number of seconds :"))
if ts>=60:
    m=ts//60
    s1=(ts%60)
if ts>=3600:
    h=ts//3600
    s2=(ts%3600)
if ts>=86400:
    d=ts//86400
    s3=(ts%86400)
print(ts,"Seconds are equal to :")
print(m,"full minute(s) and",s1,"seconds.")
print(h,"full hour(s) and",s2,"seconds.")
print(d,"full day(s) and",s3,"seconds.")

