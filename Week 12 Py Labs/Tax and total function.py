#11/17/14


def County(a):
    ctax= tp*.02
    return ctax
def State(a):
    stax= tp*.06
    return stax
def Total(a):
    total= tp+ctax+stax
    return total
tp=int(input("Please enter the price of the total purchase: "))
ctax=County(tp)
stax=State(tp)
total=Total(tp)
print("County tax =", ctax)
print("State tax =", stax)
print("Total =",total)
