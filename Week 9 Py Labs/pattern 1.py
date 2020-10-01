#This is a pattern drawing program
size=7
for r in range(size):
    for c in range(size,r,-1):
        print("*", end='')
    print()
