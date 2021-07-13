"""Tracy Worden Library of Investment Functions"""


import math
from decimal import Decimal


def present_value(fv, rr, ny):
    return Decimal(fv / (1+rr) ** ny)


def future_value(pv, rr, ny):
    return Decimal(pv * (1+rr) ** ny)


def number_years(fv, pv, rr):
    return Decimal(math.log(fv/pv)) / Decimal(math.log(1+rr))


def rate_return(fv, pv, ny):
    return Decimal((fv/pv) ** (1/ny) - 1)
