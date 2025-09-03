from part0 import *
from part0.speedingticket import speeding_ticket


def test_neg_speed():

    assert speeding_ticket(-1, -10) == 0

def test_slow_driving():

    assert speeding_ticket(40, 30) == 50



