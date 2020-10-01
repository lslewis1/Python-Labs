#11/12/14

num=[0]*10
for i in range(10):
    num[i]=int(input("Please enter a number: "))
print("Before the selection sort:")
print(num)
min=num[0]
for j in range(9):
    min=num[j]
    location=j
    for k in range(j+1,10):
        if num[k]<min:
            min=num[k]
            location=k
            tmp=num[j]
            num[j]=num[location]
            num[location]=tmp
print("After the selection sort:")
print(num)
