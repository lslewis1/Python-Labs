#10/31/14

start=int(input("What start value would you like to use? "))
end=int(input("What end value would you like to use? "))
for i in range(start,end+1,1):
    div=2
    print("Factors of",i,": ",end=' ')
    print("1",end=' ')
    while div<=i//2:
        if i%div==0:
            print(div,end=' ')
        div+=1
    print(i,end=' ')
    print()
        
    

    
       
       
