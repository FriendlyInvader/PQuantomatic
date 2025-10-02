from pquantomatic.bond.bond import bond

def test_bond():
    b = bond(face_value=1000, coupon_rate=0.05, coupon_frequency=2, maturity=10)
    assert 1000 == b.face_value
    assert 0.05 == b.coupon_rate
    assert 2 == b.coupon_frequency
    assert 10 == b.maturity
    
    