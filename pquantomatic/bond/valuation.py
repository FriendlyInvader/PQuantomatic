# Dirty price: full present value including accrued interest. Clean price = dirty − accrued interest.
# Macaulay duration: weighted average time to cashflows (years).
# Modified duration: sensitivity of price to small changes in yield = Macaulay / (1 + yield_per_period).
# Convexity: second-order sensitivity of price to yield.

import numpy as np
from scipy.optimize import newton

from pquantomatic.bond.bond import bond

class valuation:
    def __init__(self, bond:bond):
        self._bond = bond
    
    @property
    def bond(self)->bond:
        return self._bond
    
    def cashflows(self)->list[float]:
        result = [self._bond.face_value * self._bond.coupon_rate] * self._bond.maturity
        result[-1] = self._bond.face_value + result[-1]
        return result

    def price(self, ytm):
        '''
        bond price
        '''
        periods = self._bond.maturity * self._bond.coupon_frequency
        coupon = self._bond.face_value * self._bond.coupon_rate / self._bond.coupon_frequency
        discount_rate = ytm / self._bond.coupon_frequency
        price = sum([coupon / (1 + discount_rate)**t for t in range(1, periods + 1)])
        price += self._bond.face_value / (1 + discount_rate)**periods
        return price

    def yield_to_maturity(self, market_price)->float:
        '''
        YTM
        '''
        func = lambda y: self.price(y) - market_price
        # initial guess = coupon rate
        return newton(func, self._bond.coupon_rate)
