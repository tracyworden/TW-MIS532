"""Tracy Worden solution for MIS532 ex02  - This program returns the number of years it will take
for an initial investment to grow to the desired value at a given annual rate of return."""


import math


def check_input(val):
    # verify the input is an integer or float
    try:
        ret_val = int(val)
    except ValueError:
        try:
            ret_val = float(val)
        except ValueError:
            print('The input is in the wrong format, please try again.')
            ret_val = 0
            exit(1)

    return ret_val


def calculate_rate(pv, fv, rr):
    # Do the calculations
    n = math.log(fv/pv) / math.log(1+rr)
    return n


def main():
    # Ask for user input and return the number of years
    print('Welcome to the Retirement nest egg Calculator')
    input1 = input('Please enter the amount of your initial investment:')
    present_value = check_input(input1)
    input2 = input('Please enter the amount you wish your investment will grow to:')
    future_value = check_input(input2)
    input3 = input('Please enter annual rate of return you expect as a decimal (example .07):')
    rate_of_return = check_input(input3)
    n = calculate_rate(present_value, future_value, rate_of_return)
    print('Your initial investment of {} will grow to {} in {} years.'.format(present_value, future_value, n))


main()
