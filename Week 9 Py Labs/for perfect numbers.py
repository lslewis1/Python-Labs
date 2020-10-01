#10/27/14
#This program will use for loops to determine the perfect numbers between a start and end value.

start=int(input("Please enter the start value of the range: "))
end=int(input("Please enter the end value of the range: "))
for num in range(start,end+1):
    sum=0
    fac=1
    while fac<=(num//2):
        if num%fac==0:
            sum+=fac
        fac+=1
    if sum==num:
        print(num,"is a perfect number.")
