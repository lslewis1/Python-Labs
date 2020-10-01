#11/17/14

def isPrime(x):
    rem=1
    factors=2
    while factors<= x//2 and rem!=0:
        rem=x%factors
        factors+=1
    if rem!=0:
        return True
    else:
        return False
for num in range(1,101):
    if isPrime(num):
        print(num,"Is prime")
