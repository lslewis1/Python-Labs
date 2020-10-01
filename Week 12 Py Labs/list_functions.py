#11/19/14
#This is a list of valuble functions that may be imported into other programs.

def average(myList):
    sum=0
    n=len(myList)
    for i in range(n):
        sum+=myList[i]
    avg=sum/n
    return avg
