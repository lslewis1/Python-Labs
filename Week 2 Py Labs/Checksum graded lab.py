#9/12/14
#This program will be used ot determine the checksum of a code

#d is the digit currently being used
#d1 is the ones place digit
#d2 is the tens place digit
#d3 is the hundreds place digit
#d4 is the thousands place digit
#d5 is the ten thousands place digit
#d5_1 is the sum of first and last digits
#d4_2 is the sum of the second and fourth digits
#final_sum is d5_1 + d4_2
#checksum is final_sum%6

d=int(input("Plese enter a five digit number:"))
d5=d%10
d=d//10
d4=d%10
d=d//10
d3=d%10
d=d//10
d2=d%10
d1=d//10
d5_1=(d5+d1)
d4_2=(d4*d2)
final_sum=(d5_1+d4_2)
checksum=(final_sum%6)

print("The digits of the entered number are:", d1, d2, d3, d4, d5)
print("The sum of the first and last digits is:", d5_1)
print("The product of the second and fourth number is:", d4_2)
print("Final sum is:", final_sum)
print("The checksum is:", checksum)
