
n=int(input("Please enter the number of terms in the series: "))
sum=0
for tn in range(1,n+1):
    tv=1/(tn*2-1)
    if tn%2==0:
        sum-=tv
    else:
        sum+=tv
pi=4*sum
print("The estimated value of pi with the series is: ",pi)
   
    
