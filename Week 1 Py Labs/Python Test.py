# This program calculates gross pay

def main():
    #get the number of hours worked
    hours = int(input('how many hours did you work'))

    #Get the hourly pay rate
    pay_rate = float(input('Enter your hourly pay rate'))

    #Calculate the gross pay
    gross_pay = hours * pay_rate

    #Display the gross pay
    print('Gross Pay: $',format(gross_pay,',.2f'),sep='')

#Call the main function
main()
