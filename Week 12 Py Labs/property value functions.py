#11/19/14

def assesment(a):
    asmt= actual*.60
    return asmt
def proptax(a):
    ptax= (asmt//100)*.64
    return ptax
actual=int(input("What is the actual property value? "))
asmt=assesment(actual)
print("The assessment is: ",format(asmt,'.2f'))
ptax=proptax(actual)
print("The tax owed is: ",format(ptax,'.2f'))
    
    
