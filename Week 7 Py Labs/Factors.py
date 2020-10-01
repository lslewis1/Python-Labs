#10/15/14
#This program will determine all of the factors of a given number
#One and the number input are going to be printed, as they are always factors
#div is the dividing factor

x=int(input("Please enter a number :"))
print("The factors are:")
print("1")
div=2
while div<=x//2:
    if x%div==0:
        print(div)
    div+=1
print(x)
