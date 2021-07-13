"""Tracy Worden solution for MIS532 ex03  This is a calculator for PV, FV, n or r."""


import investment
from decimal import Decimal


input1 = 0
print('\nWelcome to the Calculator\n')

# Ask for user input and return the number of years
while True:
    input1 = int(input('\nEnter the value you wish to calculate for (1=PV, 2=FV, 3=n, 4=r, 5=Quit):'))
    if input1 == 5:
        break
    elif input1 == 1:
        # Calculate PV
        fv = Decimal(input('Please enter the amount you wish your investment will grow to: '))
        rr = Decimal(input('Please enter annual rate of return you expect as a decimal (example .07): '))
        ny = Decimal(input('Please enter the number of years: '))
        pv = investment.present_value(fv, rr, ny)
        print(f'You will need an initial deposit of {pv:<.2f} to grow to {fv:<.2f} in {ny} years at {rr} rate of interest.')
    elif input1 == 2:
        # Calculate FV
        pv = Decimal(input('Please enter the amount of your initial investment:'))
        rr = Decimal(input('Please enter annual rate of return you expect as a decimal (example .07): '))
        ny = Decimal(input('Please enter the number of years: '))
        fv = investment.future_value(pv, rr, ny)
        print(f'Your initial deposit of {pv:<.2f} will grow to {fv:<.2f} in {ny} years at {rr} rate of interest.')
    elif input1 == 3:
        # Calculate number of years
        pv = Decimal(input('Please enter the amount of your initial investment:'))
        fv = Decimal(input('Please enter the amount you wish your investment will grow to: '))
        rr = Decimal(input('Please enter annual rate of return you expect as a decimal (example .07): '))
        ny = investment.number_years(fv, pv, rr)
        print(f'It will take {ny:<.2f} years for your initial deposit of {pv:<.2f} to grow to {fv:<.2f} at {rr} rate of interest.')
    elif input1 == 4:
        # Calculate rate of return
        pv = Decimal(input('Please enter the amount of your initial investment:'))
        fv = Decimal(input('Please enter the amount you wish your investment will grow to: '))
        ny = Decimal(input('Please enter the number of years: '))
        rr = investment.rate_return(fv, pv, ny)
        print(f'Your rate of interest is {rr:<.2f} for your initial deposit of {pv:<.2f} to grow to {fv:<.2f} in {ny} years.')
    else:
        print('Please enter a number between 1 and 5.')
# quit
print('\nThank you for using the Calculator\n')
