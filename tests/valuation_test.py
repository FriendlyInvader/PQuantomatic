from pquantomatic.bond.valuation import valuation
from pquantomatic.bond.bond import bond

def test_cashflows():
    b = bond(face_value=1000, coupon_rate=0.05, coupon_frequency=2, maturity=10)
    v = valuation(b)

    CFs = v.cashflows()
 
    assert b.maturity == len(CFs)
    assert [50, 50, 50, 50, 50, 50, 50, 50, 50, 1050] == CFs

def test_YTM():
    b = bond(face_value=1000, coupon_rate=0.05, coupon_frequency=2, maturity=5)
    v = valuation(b)

    market_price = 1044.5200
    YTM = round(v.yield_to_maturity(market_price), 2)
    assert 0.04 == YTM

def test_bond_price():
    b = bond(face_value=1000, coupon_rate=0.05, coupon_frequency=2, maturity=5)
    v = valuation(b)

    market_price = 1044.5200
    YTM = round(v.yield_to_maturity(market_price), 2)

    price = round(v.price(YTM), 4)
    assert 1044.9129 == price
