#9/15/14
#This program uses if logic to sent a warning message to a student in danger of failing

#T1 is test one
#T2 is test two
#T3 is test three
#p_avg is the passing average
#avg is the average test sore

T1=float(input("please enter the first test score :"))
T2=float(input("please enter the second test score :"))
T3=float(input("please enter the third test score :"))
p_avg=float(input("please enter the passing test score :"))
avg=(T1+T2+T3)/3
if avg<p_avg:
    print("You are in danger of failing")
print("Your average is", avg)
print("Goodbye")

         
