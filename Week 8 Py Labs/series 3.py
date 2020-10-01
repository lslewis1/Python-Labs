#10/22/14

n=int(input("Please enter how many numbers are in the series: "))
sum=0
for tn in range(1,n+1):
    tv=tn**2
    print(tv)
    sum+=tv
print("The sum is: ",sum)
