#This is another pattern drawing program

size=7
for r in range(size,0,-1):
    print("#", end='')
    for c in range(size,r,-1):
        print(" ", end='') 
    print("#")
