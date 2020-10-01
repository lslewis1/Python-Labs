#12/1/14
#This is a Tic Tac Toe program.

board=[0]*9
winner=0
cp=1
moves=0
while moves<9 and winner==0:
    cell=int(input("Please choose your cell (0-8): "))
    while cell>8 or cell<0:
        cell=int(input("Please choose your cell (0-8): "))
    if board[cell]!=0:
        print("This cell is occupied.")
    else:
        board[cell]=cp
        if board[0]==cp and board[1]==cp and board[2]==cp:
            winner=cp
        elif board[0]==cp and board[3]==cp and board[6]==cp:
            winner=cp
        elif board[0]==cp and board[4]==cp and board[8]==cp:
            winner=cp
        elif board[1]==cp and board[4]==cp and board[7]==cp:
            winner=cp
        elif board[3]==cp and board[4]==cp and board[5]==cp:
            winner=cp
        elif board[6]==cp and board[7]==cp and board[8]==cp:
            winner=cp
        elif board[2]==cp and board[5]==cp and board[8]==cp:
            winner=cp
        elif board[2]==cp and board[4]==cp and board[6]==cp:
            winner=cp
        if winner==0:
            cp=cp%2+1
        moves+=1
        print(board[0]," ",board[1]," ",board[2])
        print(board[3]," ",board[4]," ",board[5])
        print(board[6]," ",board[7]," ",board[8])
if winner!=0:
    print("Player",cp,"is the winner.")
else:
    print("The game ended in a tie.")
