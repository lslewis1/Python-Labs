#11/10/14

import random
names=[""]*5
verbs=[""]*5
things=[""]*5
for words in range(5):
    names[words]=input("Enter a name: ")
    verbs[words]=input("Enter a verb: ")
    things[words]=input("Enter a thing: ")
for j in range(1,8):
    n1=random.randint(0,4)
    n2=random.randint(0,4)
    n3=random.randint(0,4)
    print(names[n1],verbs[n2],things[n3])
