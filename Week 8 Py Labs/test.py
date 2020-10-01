n=int(input("number is: "))
sum=0
for tn in range(1,n+1):
    tv=tn
    if tn%3==0:
        sum-=tv
    else:
        sum+=tv
print(sum)
