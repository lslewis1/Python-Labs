#12/3/14
#Chutes and Ladders

import random
brd=[0]*100
p1=0
p2=0
winner=0
dice=0
position=0
cp=1
brd[19]=-10
brd[47]=-15
brd[65]=-20
brd[98]=-50
brd[4]=10
brd[27]=12
brd[63]=20
brd[96]=3

while winner==0:
    if cp==1:
        x=input("\nPlayer 1, press any key to roll your dice.")
        dice=random.randint(1,7)
        pos=p1+dice
        if pos<=99:
            if brd[pos]>0:
                print("Player 1, you have landed on a ladder.")
            if brd[pos]<0:
                print("Player 1, you have landed on a shute.")
            p1=pos+brd[pos]
        else:
            print("Sorry, you cannot make a move.")
        if p1==99:
            winner=p1
            print("Player 1 wins.")
        else:
            cp=2
    else:
        if cp==2:
            x=input("\nPlayer 2, press any key to roll your dice.")
            dice=random.randint(1,7)
            pos=p2+dice
            if pos<=99:
                if brd[pos]>0:
                    print("Player 2, you have landed on a ladder.")
                if brd[pos]<0:
                    print("Player 2, you have landed on a shute.")
                p2=pos+brd[pos]
            else:
                print("Sorry, you cannot make a move.")
            if p2==99:
                winner=p2
                print("Player 2 wins.")
            else:
                cp=1
    for i in range(99,-1,-1):
        if i%10==0:
            print("")
        if i==p1 and i==p2:
            print(" 12 ",end="")
        elif i==p1:
            print(" 1  ",end="")
        elif i==p2:
            print(" 2  ",end="")
        else:
            print(" -- ",end="")
 
