#10/22/14

n=int(input("Please enter how many numbers are in the series: "))
sum=1
print("1")
for tn in range(2,n+1):
    tv=1/(tn**2-1)
    print("1/(",tn,"*",tn**2-1,")=",tv)
    sum+=tv
print("The sum is: ",sum)
