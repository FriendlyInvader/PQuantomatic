# Face / par value: principal repaid at maturity (e.g. 100 or 1000).
# Coupon: annual coupon rate (e.g. 0.05 = 5%). If semiannual, coupon payments = coupon_rate/2 × par.
# Yield to maturity (YTM): interest rate that makes PV of cashflows = price.

class bond:
    def __init__(self, face_value:float, coupon_rate:float, coupon_frequency:int, maturity:int):
        self._face_value = face_value
        self._coupon_rate = coupon_rate
        self._coupon_frequency = coupon_frequency
        self._maturity = maturity

    @property
    def face_value(self)->float:
        return self._face_value

    @property
    def coupon_rate(self)->float:
        return self._coupon_rate

    @property
    def coupon_frequency(self)->int:
        return self._coupon_frequency
    
    @property
    def maturity(self)->int:
        return self._maturity
