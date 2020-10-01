def reverse(a):
    ones=a%10
    a=a//10
    tens=a%10
    a=a//10
    hund=a%10
    thousands=a//10
    a=ones*1000+tens*100+hund*10+thousands
    return a
x=int(input("Please enter a four digit number: "))
a=reverse(x)
print(a)
